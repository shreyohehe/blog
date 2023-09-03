from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Posts
def index(request):
    post= Posts.objects.all()

    return render(request,'index.html',{'post': post})
def post(request,ok):
    pt=Posts.objects.get(id=ok)

    return render(request,'post.html',{'pt': pt})
