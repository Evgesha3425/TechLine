from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Goods, Good_category

menu = ['Главная страница', 'Каталог', 'Новости', 'Личный кабинет']


def index(request):
    categories = Good_category.objects.all()
    goods = Goods.objects.all()

    context = {
        'title': 'Главная страница',
        'categories': categories,
        'goods': goods,
    }

    return render(request, 'catalog/index.html', context=context)


def catalog(request):
    goods = Goods.objects.all()
    return render(request, 'catalog/catalog.html', {'goods': goods, 'title': 'Каталог'})


def show_good(request, good_id):
    return HttpResponse(f'Отображение товара с id = {good_id}')


def show_category(request, cat_id):
    cats = Good_category.objects.filter(id=cat_id)

    if len(cats) == 0:
        raise Http404()

    context = {
        'title': 'Отображение по категориям',
        'cats': cats,
        'cat_selected': cat_id,
    }

    return render(request, 'catalog/index.html', context=context)


def account(request):
    return render(request, 'catalog/account.html', {'title': 'Личный кабинет'})


def news(request):
    return render(request, 'catalog/news.html', {'title': 'Новости'})
