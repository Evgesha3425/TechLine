from django.shortcuts import render
from django.http import HttpResponse

from .models import Goods

# menu = ['Главная страница', 'Каталог']


def index(request):
    return render(request, 'catalog/index.html', {'title': 'Главная страница'})


def catalog(request):
    goods = Goods.objects.all()
    return render(request, 'catalog/catalog.html', {'goods': goods, 'title': 'Каталог'})


def for_test(request):
    return render(request, 'catalog/for_test.html', {'title': 'Для теста'})
