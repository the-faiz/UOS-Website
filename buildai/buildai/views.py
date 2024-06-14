from django.shortcuts import render, redirect


def home(request):
    return render(request,'Home_Page/home.html')


def login(request):
    return render(request,'User/login.html')


def signup(request):
    return render(request,'User/signup.html')


def subscribe(request):
    return render(request,'Subscription/subscribe.html')