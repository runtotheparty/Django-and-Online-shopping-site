from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def index(request):
    return render(request, "index.html")

def online_shop(request):
    return render(request, "Online shop.html")

def about_me(request):
    return render(request, "About me.html")