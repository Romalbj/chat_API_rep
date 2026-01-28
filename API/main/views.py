from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello, world!</h1><p>This is an HTTP response with HTML tags.</p>")
