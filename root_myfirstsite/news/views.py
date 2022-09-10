from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import News, Category
from .forms import NewsForm


# Create your views here.
def index(request):
    # print(request)
    news = News.objects.all()  # order_by('-created_at') можно использовать сортировку тут вместа мета класса в модуле
    # res = '<h1>Список новостей</h1>'
    # for item in news:
    #     res += f'<div>\n<p>{item.title}</p>\n<p>{item.content}</p>\n</div>\n<hr>'
    # return HttpResponse(res)
    # categories = Category.objects.all()
    return render(request, 'news/index.html', {'news': news,
                                               'title': 'Список новостей'})  # для большого контекста можно создать переменную со словарём


def test(requets):
    # name = input('enter your name: ')
    name = 'хозяйка'
    return HttpResponse(f'<h1>Это тестовая страница, {name}</h1>')


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    # category = Category.objects.get(pk=category_id)
    category = get_object_or_404(Category, pk=category_id)
    context = {'news': news,
               'category': category}
    return render(request, 'news/category.html', context)


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, 'news/view_news.html', {'news_item': news_item})


def add_news(request):
    if request.method == 'POST':
        pass
    else:
        form = NewsForm()
    return render(request, 'news/add_news.html', {'form': form})