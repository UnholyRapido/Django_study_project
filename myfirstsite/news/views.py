from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.
def index(request):
    # print(request)
    return HttpResponse('Hello world!')

def test(requets):
    # name = input('enter your name: ')
    name = 'хозяйка'
    return HttpResponse(f'<h1>Это тестовая страница, {name}</h1>')