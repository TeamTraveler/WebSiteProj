<<<<<<< HEAD
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from .models import UserInfo
from django import forms

=======
import json

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from .models import User, Post
from django.views.generic import ListView
from rest_framework.response import Response
from rest_framework.views import APIView
>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26

# Create your views here.

def show_post(request):
    return render(
        request,
<<<<<<< HEAD
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
=======
        'post/index.html'
    )

class PostList(ListView):
    model = Post

def show_post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(
        request,
        'post/post_detail.html',
        {
            'post':post,
        }
>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26
    )


def login(request):
<<<<<<< HEAD
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
=======
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, user_name=username, password=password)
        # print(username,password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return redirect('/'), {'error': 'username or password is incorrect'}
    else:
        return render(request, 'post/login.html')


@csrf_exempt
def register(request):
    data = request.POST
    template_name = "login.html"
    if User.objects.filter(id=data.get('username')).exists():
        context = {
            "result": "이미 존재하는 아이디입니다."
        }
        return redirect('post/register.html')
    elif data.get('password1') != data.get('password2') :
        context = {
            "result": "비밀번호가 다릅니다."
        }
    else:
        User.objects.create(
            username=data.get('username'),
            password=data.get('password1'),
>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26
        )
        context = {
            "result": "회원가입 성공"
        }
<<<<<<< HEAD
        return redirect('home')
=======
        return redirect('post/index.html')
>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26


@csrf_exempt
def loginCheck(request):
    template_name = 'login.html'
    request.session['loginOk'] = False
<<<<<<< HEAD
    try:
        data = request.POST
        inputId = data.get('id')
        inputPassword = data.get('passwd')

    except (KeyError, inputId == "", inputPassword == ""):
=======
    inputId == ''
    inputPassword == ''
    
    try:
        data = request.POST
        inputId = data['username']
        inputPassword = data['password']

    except (KeyError):
>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26
        context = {
            "uid": "empty",
            "upass": "empty",
        }
<<<<<<< HEAD
        return redirect('home')
    else:
        if UserInfo.objects.filter(id=inputId).exists():
            getUser = UserInfo.objects.get(id=inputId)
            if getUser.passwd == inputPassword:
=======
        return render(request, template_name, context)
    else:
        if User.objects.filter(username=inputId).exists():
            getUser = User.objects.get(username=inputId)
            if getUser.password == inputPassword:
>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26
                request.session['loginOk'] = True
                context = {
                    "result": "로그인 성공"
                }
<<<<<<< HEAD
                return redirect('home', context)
=======
>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26
            else:
                request.session['loginOk'] = False
                context = {
                    "result": "비밀번호가 틀렸습니다"
                }
<<<<<<< HEAD
                return redirect('login')
=======
>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26
        else:
            request.session['loginOk'] = False
            context = {
                "result": "존재하지 않는 id입니다"
            }
<<<<<<< HEAD
            return redirect('home')
=======
        return HttpResponse(json.dumps(context), content_type="application/json")

# pip install djangorestframework
class Uploadfile(APIView):
    # @csrf_exempt
    def get(self,request):
        post=Post.objects.all()
        return render(request,"post/upload.html",context=dict(post=post)) 
    @csrf_exempt
    def post(self,request):
        title=request.data.get('title')
        content=request.data.get('content')
        user_id=request.data.get('user_id')
        file_org=request.FILES.getlist('file_org')
        # 닉네임에 따른 이미지
        post=Post()
        post.title=title
        post.content=content
        # post.save()
        for images in file_org:
            # post.author=nickname
            post.head_image=images
            post.save()
        # post.head_image=file_org
        # post.save()


        # print(user_id)
        return Response(status=200)

>>>>>>> 5d04df48e53cb2aac05e4641847bee4b77cb7b26
