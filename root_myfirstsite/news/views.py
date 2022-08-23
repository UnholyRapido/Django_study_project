from django.shortcuts import render
from django.http import HttpResponse

from .models import News


# Create your views here.
def index(request):
    # print(request)
    news = News.objects.order_by('-created_at')
    # res = '<h1>Список новостей</h1>'
    # for item in news:
    #     res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>'
    # return HttpResponse(res)
    return render(request, 'news/index.html', {'news': news, 'title': 'Список новостей'})  # для большого контекста можно создать переменную со словарём

def test(requets):
    # name = input('enter your name: ')
    name = 'хозяйка'
    return HttpResponse(f'<h1>Это тестовая страница, {name}</h1>')