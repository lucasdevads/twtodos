from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, "todos/home.html")


def page(request):
    return render(request,)