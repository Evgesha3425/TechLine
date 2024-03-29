from django.conf.urls.static import static
from django.urls import path

from catalog import views
from catalog.views import *
from techline import settings

urlpatterns = [
    path('', index, name='home'),
    path('catalog/', catalog, name='catalog'),
    path('categories/', show_category, name='categories'),
    path('good/<int:good_id>', show_good, name='good'),
    path('account/', account, name='account'),
    path('news/', news, name='news'),
]
