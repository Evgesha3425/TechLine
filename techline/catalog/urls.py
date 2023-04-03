from django.conf.urls.static import static
from django.urls import path

from catalog import views
from catalog.views import *
from techline import settings

urlpatterns = [
    path('', index, name='home'),
    path('catalog', catalog, name='catalog'),
    path('good/<int:good_id>', show_good, name='good'),
    path('for_test', for_test, name='test'),
    path('category/<int:cat_id>', show_category, name='category')
]
