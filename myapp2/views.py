from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.



def v1(request):
    return HttpResponse('<h1>This is First View of Myapp2 </h1>')


def v2(request):
    return HttpResponse('<h1>This is Second View of Myapp2 </h1>')


def v3(request):
    return HttpResponse('<h1>This is Third View of Myapp2 </h1>')

