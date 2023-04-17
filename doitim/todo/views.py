from multiprocessing import context
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404, JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Item
from .forms import TodoForm
from django.utils import timezone
from datetime import date, datetime, timedelta
from django.urls import reverse
import pytz


class TodoList:
    def __init__(self, request: object) -> None:
        self.tz_name = request.session.get('django_timezone', 'Asia/Shanghai')
        timezone.activate(pytz.timezone(self.tz_name))
        self.user_today = timezone.localtime(timezone.now()).date()
        self.todos = Item.objects.filter(
            owner_id=request.user.id, is_deleted = False).order_by('-date_added')
        self.title = "所有"

    def get_todos(self):
        return self.todos


class TodayTodoList(TodoList):
    def __init__(self, request: object) -> None:
        super().__init__(request)
        self.title = "今天"

    def get_todos(self):
        todos = self.todos.filter(start_date=self.user_today)
        return todos


class TomorrowTodoList(TodoList):
    def __init__(self, request: object) -> None:
        super().__init__(request)
        self.title = "明天"

    def get_todos(self):
        tomorrow = self.user_today + timedelta(days=1)
        todos = self.todos.filter(start_date=tomorrow)
        return todos


class Next7DaysTodoList(TodoList):
    def __init__(self, request: object) -> None:
        super().__init__(request)
        self.title = "最近 7 天"

    def get_todos(self):
        the_7th_day_from_today = self.user_today + timedelta(days=6)
        todos = self.todos.filter(start_date__date__range=(
            self.user_today, the_7th_day_from_today))
        return todos


def all(request):
    todo_list = TodoList(request)
    context = {
        'title': todo_list.title,
        'todos': todo_list.get_todos(),
        'form': TodoForm()
    }
    return render(request, 'todo/index.html', context)


@login_required
def today(request):
    todo_list = TodayTodoList(request)
    context = {
        'title': todo_list.title,
        'todos': todo_list.get_todos(),
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
def add_or_update_todo(request):
    if request.method == 'POST':
        if request.POST.get('todo_id'):
            todo = get_object_or_404(Item, pk=request.POST.get(
                'todo_id'), owner_id=request.user)
            print(request.POST.get('delete'))
            if request.POST.get('delete'):
                todo.is_deleted = True
                todo.save()
                return HttpResponse("删除成功：" + todo.desc)
            form = TodoForm(request.POST, instance=todo)
            if form.is_valid():
                form.save()
            return HttpResponse("修改成功")
        else:
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
