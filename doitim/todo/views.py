from multiprocessing import context
import re
from typing import Text
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Item
from .forms import ItemForm
from django.utils import timezone
from datetime import date, datetime,timedelta
from django.urls import reverse
import pytz

@login_required
def index(request, slug='today'):
    todolists = TodoList().todolists
    todos = Todos.todos()
    print("hello")
    print(reverse('todo:js_catlog'))
    context = {
        'todolists': todolists,
        'slug': slug,
        'todos':todos,
        'form':ItemForm()
    }
    return render(request, "todo/index.html", context)

# 收件箱
@login_required
def inbox(request):
    # get some data
    data = None
    menu = ('inbox', 'today', 'tomorrow', 'next')
    context = {
        'data' : data,
        'menus': menu,
        'now' : menu[0]
    }
    return render(request, "todo/inbox.html", context)

# 今日待办
@login_required
def today_v2(request):
    # get some data
    data = None
    menu = ('inbox', 'today', 'tomorrow', 'next')
    context = {
        'data' : data,
        'menus': menu,
        'now' : menu[1]
    }
    return render(request, "todo/inbox.html", context)


@login_required
def item_form(request):
    form = ItemForm()
    print(form)
    return render(request, "todo/item_form.html", {'form': form})

@login_required
def home(request):
    menu = Menu()
    context = {
        'menus':menu.menu
    }
    return render(request, 'todo/home.html',context)

@login_required
def new_item(request):
    # 添加新事务
    if request.method == 'POST':

        # form = ItemForm(request.POST)
        print(request.POST.get("start_date_0"))
        datetime_string = request.POST.get("start_date_0") + " " + request.POST.get("start_date_1")
        start_date = datetime.strptime(datetime_string, "%Y-%m-%d %H:%M:%S")
        print(request.POST.get("desc"))

        # 这里还有问题，form 实例还不知道怎么创建

        # form = ItemForm()
        # form.desc = request.POST.get("desc")
        # form.start_date = start_date
        # if form.is_valid():
        #     instance = form.save(commit=False)
        #     instance.desc = form.cleaned_data['desc']
        #     instance.start_date = form.cleaned_data['start_date']
        #     instance.owner_id = request.user.id
        #     # instance.start_date = date.today()
        #     print("2333",form.cleaned_data)
        #     # instance.start_date = form.cleaned_data['start_date']
        #     print(instance.start_date)
        #     print("test", timezone.is_naive(instance.start_date),instance.start_date.tzinfo)
        #     print(timezone.now(), timezone.is_aware(timezone.now()))
        #     instance.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

@login_required
def today(request):
    # start = datetime.now().date().astimezone(pytz.utc)
    start = datetime.combine(datetime.now().date(), datetime.min.time()).astimezone(pytz.utc)
    end = start + timedelta(days = 1)
    today = Item.objects.filter(start_date__range = [start, end]).order_by('-date_added')
    # test = Item.objects.filter(id =2 )[0].start_date
    # d = date.today()
    # d2 = datetime.combine(d, datetime.min.time()).astimezone(pytz.utc)
    # # d3 = now().date().astimezone(pytz.utc)
    # print(d2<test, start, end)
    form = ItemForm()
    context = {
        'today': today,
        'form': form,
    }
    return render(request, 'todo/today.html', context)

class Todos():
    def todos(filter = ''):
        todos = Item.objects.order_by('-date_added')
        return todos

class TodoList(object):
    todolists = {
        'inbox':{
            'name':'inbox',
            'icon':'inbox',
            'title':'inbox'
        },
        'today':{
            'name':'today',
            'icon':'sun',
            'title':'today'
        },
        'tomorrow':{
            'name':'tomorrow',
            'icon':'calendar',
            'title':'tomorrow'
        },
        'next':{
            'name':'next',
            'icon':'hourglass',
            'title':'next',
        },
    }
