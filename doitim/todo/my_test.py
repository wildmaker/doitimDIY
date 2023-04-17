from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.shortcuts import render
from .forms import TodoForm
from .models import Item

# class AdminTimeWidget2(AdminTimeWidget):
#     class Media:
#         extend = False
#         js = [
#             "js/calendar.js",
#             "js/DateTimeShortcuts.js",
#         ]

# w  = AdminTimeWidget2()
# print(w.media)

# class AdminSplitDateTime2(AdminSplitDateTime):
#     def __init__(self, attrs=None):
#         widgets = [AdminDateWidget,AdminTimeWidget2]
#         forms.MultiWidget.__init__(self, widgets, attrs)


class TestForm(forms.Form):
    from_date = forms.DateField(widget=AdminDateWidget)

def test(request):
    today_first_dodo = Item.objects.filter(owner_id = request.user).order_by('-date_added').first()
    form = TodoForm(instance=today_first_dodo)
    todo_id = today_first_dodo.id
    return render(request,'todo/test.html', {'form':form,'todo_id':todo_id})

def test2(request):
    # name =  "<a href=’/accounts’>233</a>"
    form1 = TodoForm()
    return render(request,'todo/test.html', {'form1':form1})