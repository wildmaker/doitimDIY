from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.views import LoginView
def userlogin(request):
    """用户登录"""
    if request.method != "POST":
        context = {}
    else:
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            # redirect
            return HttpResponseRedirect(reverse("todo:pages", kwargs = {'index': 0}))
        else:
            # return an error message
            context = {"error_message":"Could not log in, please check your accout."}
        
    return render(request,'users/login.html', context)


# 注销
def userlogout(request):
    """注销用户"""
    logout(request)
    return HttpResponseRedirect(reverse("todo:index"))

# 注册
from django.contrib.auth.forms import UserCreationForm

def register(request):
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
            authenticated_user = authenticate(username = new_user.username, 
                password = request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('todo:index'))
    
    context = {'form': form}
    return render(request, 'users/register.html', context)

