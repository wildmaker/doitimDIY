from django.forms import ModelForm, TextInput, TimeInput, DateTimeInput, HiddenInput
from django import forms
from .models import Item
from django.contrib.admin.widgets import AdminSplitDateTime, AdminTimeWidget, AdminDateWidget


class TestForm(forms.Form):
    from_date = forms.DateField(widget=AdminDateWidget)


class MySplitDateTime(AdminSplitDateTime):
    template_name = "todo/split_datetime.html"


# class TodayTodoForm(ModelForm):
#     class Meta:
#         model = Item
#         fields = ['desc', 'start_date']
#         labels = {
#             'desc': '',
#             'start_date': ''
#         }
#         widgets = {
#             'desc': TextInput(attrs={'class': 'form-control form-control-lg', 'id': 'exampleFormControlInput1', 'placeholder': '添加“今天”的任务至“收集箱”'}),
#             'start_date': HiddenInput()
#         }


class TodoForm(ModelForm):
    class Meta:
        model = Item
        fields = ['desc', 'start_date',]