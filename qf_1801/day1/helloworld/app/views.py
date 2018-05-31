from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def first_hello(request):

    return HttpResponse('hello world')

def girl_hello(request):
    print(request)
    return HttpResponse('hello 美女！')
