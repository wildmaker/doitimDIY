from django.test import TestCase
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Item
import pytz
from datetime import datetime,time

# Create your tests here.
def send_post(request):
    if request.method == 'POST':
        data = {
            "姓名":"张寒冰",
            "年龄":"29",
        }
        # new_todo()
        test_time_compare()
        return JsonResponse(data)
    else:
        return render(request,'tests/send_post_btn.html')

def new_todo():
    # 创建一个 UTC 不在同一天，但本地时间在同一天的任务
    start_date_without_tz = datetime(2023,10,14,23,59,59,999999)
    tz = pytz.timezone('Asia/Shanghai')
    start_date = tz.localize(start_date_without_tz)
    print(start_date)

    todo_1 = Item(desc='午夜待办4',owner_id=4,start_date=start_date)
    todo_1.save()

def test_time_compare():
    today_without_tz = datetime(2023,10,14,0,0,0)
    tz = pytz.timezone('Asia/Shanghai')
    today = tz.localize(today_without_tz)
    today_date = today.date()
    today_min = tz.localize(datetime.combine(today_date,today.min.time()))
    today_max = tz.localize(datetime.combine(today_date,today.max.time()))

    print(today)
    print(today_min,today_max)
    now = timezone.now()
    print('now',now,timezone.is_aware(now),now.tzinfo)

    todos = Item.objects.filter(
            owner_id=4, 
            start_date__range = (today_min,today_max)
        )