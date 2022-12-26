from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(reqest):
    return HttpResponse('<h1>This is my firt url projrect<h2>')
