from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.shortcuts import render
from .forms import ItemForm

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
    # name =  "<a href=’/accounts’>233</a>"
    form1 = ItemForm()
    form2 = TestForm()
    return render(request,'todo/test.html', {'item_form':form1, 'form2':form2})

def test2(request):
    # name =  "<a href=’/accounts’>233</a>"
    form1 = ItemForm()
    return render(request,'todo/test2.html', {'form1':form1})