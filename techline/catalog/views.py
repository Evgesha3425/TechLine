from django.shortcuts import render, get_object_or_404
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


def show_category(request, category_id):
    category = get_object_or_404(Goods, pk=category_id)

    context = {
        'title': category.name,
        'category': category,
        'cat_selected': category.category_id,
    }

    return render(request, 'catalog/categories.html', context=context)


def account(request):
    return render(request, 'catalog/account.html', {'title': 'Личный кабинет'})


def news(request):
    return render(request, 'catalog/news.html', {'title': 'Новости'})
