"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.shortcuts import HttpResponse,render,redirect
from mycode import views


def index(requeust):
    return HttpResponse("indexaaa")


def login(request):
    #return HttpResponse('登录成功！')
    if request.method == "GET":
        return render(request,'login.html')
    else:
        user = request.POST.get('username')
        passwd = request.POST.get('password')
        if user=='admin' and passwd=='123456':
            # return redirect('http://www.baidu.com')
            # return redirect("/index/")
            return render(
                request,
                'index.html',
                {'name':'alex',
                 'users':['李一','李二'],
                 'user_dict':{'key1':'value1','key2':'value2'},
                 'user_list_dict':[
                     {'id':1,'name':"Tom",'sex':'boy'},
                     {'id':2,'name':"John",'sex':'boy'},
                     {'id':3,'name':"Smile",'sex':'girl'}
                 ]}
            )
        else:
            return render(request, 'login.html',{'msg':'用户名或密码错误！'})





urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login),
    path('index/',index),
    path('classes/',views.classes),
    path('add_class/',views.add_class),
    path('del_class/',views.del_class),
    path('edit_class/',views.edit_class),
]
