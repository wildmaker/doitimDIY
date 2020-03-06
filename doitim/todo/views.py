from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import json

def index(request):
    """学习笔记的主页"""
    return render(request, 'todo/index.html')

from .forms import ItemForm
from .models import Item
@login_required
def new_item(request):
    """添加新事务"""
    if request.method != 'POST':
        # 未提交数据:创建一个新表单d
        pass
    else:
        # 创建新的事务
        desc = json.loads(request.body).get('desc')
        Item.objects.create(desc = desc, owner = request.user)
        form = ItemForm(request.POST)
        if form.is_valid():
            new_item = form.save(commit = False)
            new_item.owner = request.user
            new_item.save()
            
        
