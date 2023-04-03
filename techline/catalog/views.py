from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Goods, Good_category

# menu = ['Главная страница', 'Каталог']


def index(request):
    cats = Good_category.objects.all()

    context = {
        'title': 'Главная страница',
        'cats': cats,
        'category_selected': 0,
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


def for_test(request):
    return render(request, 'catalog/for_test.html', {'title': 'Для теста'})
