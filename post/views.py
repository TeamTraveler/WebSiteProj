from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import UserInfo
from django import forms


# Create your views here.

def show_post(request):
    return render(
        request,
        'post/index.html',
    )


def search_page(request):
    return render(
        request,
        'post/search_page.html',
    )


def register(request):
    form = UserInfo()
    return render(
        request,
        'post/register.html',
    )


def login(request):
    return render(
        request,
        'post/login.html',
    )


@csrf_exempt
def signup(request):
    data = request.POST
    if UserInfo.objects.filter(id=data.get('username')).exists():
        context = {
            "result": "/"
        }
        return redirect('register')
    elif data.get('password1') != data.get('password2'):
        context = {
            "result": "비밀번호가 다릅니다."
        }
        return redirect('register')
    elif UserInfo.objects.filter(id=data.get('nickname')).exists():
        return redirect('register')
    else:
        UserInfo.objects.create(
            id=data.get('username'),
            nickname=data.get('nickname'),
            passwd=data.get('password1'),
        )
        context = {
            "result": "회원가입 성공"
        }
        return redirect('home')


@csrf_exempt
def loginCheck(request):
    template_name = 'login.html'
    request.session['loginOk'] = False
    try:
        data = request.POST
        inputId = data.get('id')
        inputPassword = data.get('passwd')

    except (KeyError, inputId == "", inputPassword == ""):
        context = {
            "uid": "empty",
            "upass": "empty",
        }
        return redirect('home')
    else:
        if UserInfo.objects.filter(id=inputId).exists():
            getUser = UserInfo.objects.get(id=inputId)
            if getUser.passwd == inputPassword:
                request.session['loginOk'] = True
                context = {
                    "result": "로그인 성공"
                }
                return redirect('home', context)
            else:
                request.session['loginOk'] = False
                context = {
                    "result": "비밀번호가 틀렸습니다"
                }
                return redirect('login')
        else:
            request.session['loginOk'] = False
            context = {
                "result": "존재하지 않는 id입니다"
            }
            return redirect('home')
