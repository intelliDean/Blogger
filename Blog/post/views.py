from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def hello(request):
    return render(request, 'hello.html')


def name(request):
    return render(request, 'name.html')


def welcome(request):
    return HttpResponse("Dean, Welcome to Djando Class")


def intro(request):
    first_name = "Dean"
    last_name = "Michael"
    money = "$10,000"
    return HttpResponse(f"My name is {last_name} {first_name} and I earn {money} monthly")
