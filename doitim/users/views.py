from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from django.contrib import auth

# 注册
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('todo:today'))
    """ 注册新用户 """
    if request.method != 'POST':
        # print('hello')
        # 显示空的注册表单
        form = UserCreationForm()
    else:
        # 处理填写好的表单
        form = UserCreationForm(data = request.POST)

        if form.is_valid():
            new_user = form.save()
            # 让用户自动登录, 再重定向到主页
            authenticated_user = auth.authenticate(username = new_user.username, 
                password = request.POST['password1'])
            auth.login(request, authenticated_user)
            return HttpResponseRedirect(reverse('todo:today'))
    
    context = {'form': form}
    return render(request, 'users/register.html', context)


def login(request):
    """用户登录"""
    if request.method != "POST":
        context = {}
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse("todo:today"))
        else:
            # return an error message
            context = {"error_message":"Could not log in, please check your accout."}
        
    return render(request,'users/login.html', context)


# 注销
def logout(request):
    """注销用户"""
    auth.logout(request)
    return HttpResponseRedirect(reverse('homepage:index'))


