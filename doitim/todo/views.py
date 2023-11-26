from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest, HttpResponseNotAllowed
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Item
from .forms import TodoForm
from django.utils import timezone
from datetime import date, datetime, timedelta
from django.urls import reverse
import pytz
import json
from django.core import serializers
from django.middleware import csrf
import pprint

class TodoList:
    def __init__(self, request: object) -> None:
        self.todos = Item.objects.filter(
            owner_id=request.user.id, is_deleted = False).order_by('-date_added')
        self.title = "所有"
        self.tz = request.COOKIES.get('timezone',None)
        print('self.tz',self.tz)

    def next_7_days(self):
        range_min = timezone.now()-timedelta(days=1)
        range_max = timezone.now()+timedelta(days=7)
        todos = self.todos.filter(start_date__date__range=(range_min,range_max))
        return todos

class TodayTodoList(TodoList):
    def __init__(self, request: object) -> None:
        super().__init__(request)
        self.title = "今天"


class TomorrowTodoList(TodoList):
    def __init__(self, request: object) -> None:
        super().__init__(request)
        self.title = "明天"

def all(request):
    todo_list = TodoList(request)
    context = {
        'title': todo_list.title,
        'todos': todo_list.todos,
        'form': TodoForm()
    }
    return render(request, 'todo/index.html', context)

@login_required
def today(request):
    todo_list = TodoList(request)
    tz = timezone.get_current_timezone()
    today = timezone.localtime(timezone.now())
    today_date = today.date()
    today_min =timezone.make_aware(datetime.combine(today_date,today.min.time()),tz)
    today_max =timezone.make_aware(datetime.combine(today_date,today.max.time()),tz)
    todos = todo_list.todos.filter(start_date__range=(today_min,today_max))
    context = {
        'title': todo_list.title,
        'todos': todos,
        'form': TodoForm(),
    }
    return render(request, 'todo/index.html', context)

@login_required
def tomorrow(request):
    todo_list = TomorrowTodoList(request)
    context = {
        'title': todo_list.title,
        'todos': todo_list.get_todos(),
        'form': TodoForm(),
    }
    return render(request, 'todo/index.html', context)


@login_required
def next_7_days(request):
    todo_list = Next7DaysTodoList(request)
    context = {
        'title': todo_list.title,
        'todos': todo_list.get_todos(),
        'form': TodoForm(),
    }
    return render(request, 'todo/index.html', context)

@login_required
def new(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.owner = request.user
            todo.date_added = datetime.now()
            form.save()
    else:
        form = TodoForm()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        todo_id = data.get('todo_id')
        print('tz_info_1', timezone.get_current_timezone())
        if todo_id:
            todo = get_object_or_404(Item, pk=todo_id, owner_id=request.user)
            if data.get('delete'):
                todo.is_deleted = True
                todo.save()
                return HttpResponse("删除成功：" + todo.desc)
            else:
                new_todo_data = {
                    'desc':data.get('desc'),
                    'csrfmiddlewaretoken':csrf.get_token(request),
                    # 'start_date':todo.start_date,
                    # 'start_date':'2023-11-06T16:41'
                }
                form = TodoForm(new_todo_data, instance=todo)
                if form.is_valid():
                    form.save()
                    print('tz_info', timezone.get_current_timezone())
                    return HttpResponse("修改成功")
                else:
                    return HttpResponse("表单不对")
        else:
            return HttpResponseBadRequest('ID is missing.')
    return HttpResponseNotAllowed(['POST'])

@login_required
def index(request, slug='today'):
    # 如果 slug
    todos = Todos.todos()
    context = {
        'slug': slug,
        'todos': todos,
        'form': TodoForm()
    }
    return render(request, "todo/index.html", context)

# 今日待办


@login_required
def today_v2(request):
    # get some data
    data = None
    menu = ('inbox', 'today', 'tomorrow', 'next')
    context = {
        'data': data,
        'menus': menu,
        'now': menu[1]
    }
    return render(request, "todo/inbox.html", context)


class Todos():
    def todos(filter=''):
        todos = Item.objects.order_by('-date_added')
        return todos
