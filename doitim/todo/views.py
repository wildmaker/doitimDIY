from typing import Text
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, JsonResponse, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from .models import Item
from .forms import ItemForm
from django.utils.timezone import now, timedelta
from datetime import date, datetime
import pytz


# 主页
def index(request):
    return render(request, 'todo/index.html')

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
def pages(request, index):
    if not index: 
        index = 0
        print("not")
    else:
        index = int(index)
    menu = Menu().menu
    print(menu[index])
    data = {
        'title': menu[index]
    }
    context = {
        'data': data,
        'menu': menu,
        'index': menu[index]
    }
    return render(request, "todo/pages.html", context)

@login_required
def home(request):
    menu = Menu()
    context = {
        'menus':menu.menu
    }
    return render(request, 'todo/home.html',context)

@login_required
def items(request):
    items = Item.objects.order_by('-date_added')
    form = ItemForm()
    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'todo/items.html', context)

@login_required
@csrf_exempt
def new_item(request):
    """添加新事务"""
    if request.method != 'POST':
        # 未提交数据:创建一个新表单
        form = ItemForm()
        context = {'form':form}
        return render(request,'todo/new_item.html', context)
    else:
        # 创建新的事务
        form = ItemForm()
        desc = json.loads(request.body).get('desc')
        new_item = form.save(commit = False)
        new_item.owner = request.user
        new_item.start_date = None
        new_item.desc = desc
        new_item.save()
        messages.add_message(request, messages.INFO, 'hello world!')
        return JsonResponse({'foo':'bar'})

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

class TodoList():
    pass

class Test(object):
    test = 2
    
    
class Menu(object):
    menu = ('inbox', 'today', 'tomorrow', 'next')