"""fortraveler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
<<<<<<< HEAD
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_post, name='home'),
    path('login.html/', views.login, name='login'),
    path('register.html/', views.register, name='register'),
    path('login.html/register.html/', views.register),
    path('search_page.html/', views.search_page),
    path('register.html/signup/', views.signup),
    path('login.html/loginCheck/', views.loginCheck)
=======
from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

app_name = 'post'

urlpatterns = [
    path('', views.show_post),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='before_register'),
    path('login/register/', views.register, name='after_register'),
    path('post/', views.PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', views.show_post_detail),
    path('upload/',csrf_exempt(views.Uploadfile.as_view()), name='upload')
    
>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26
]
