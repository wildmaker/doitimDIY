from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, JsonResponse
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



def index(request):
    """学习笔记的主页"""
    return render(request, 'todo/index.html')

@login_required
def home(request):
    return render(request, 'todo/home.html')

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
    else:
        # 创建新的事务
        form = ItemForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit = False)
            new_item.owner = request.user
            new_item.start_date = None
            new_item.save()
        # return HttpResponseRedirect(reverse('todo:items'))
    context = {'form':form}
    return render(request,'todo/new_item.html', context)
        # desc = json.loads(request.body).get('desc')
        # Item.objects.create(desc = desc, owner = request.user)
        # form = ItemForm(request.POST)
        # if form.is_valid():
        #     new_item = form.save(commit = False)
        #     new_item.owner = request.user
        #     new_item.save()
        #     messages.add_message(request, messages.INFO, "helloworld")
            
        

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