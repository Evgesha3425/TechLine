from django.conf.urls.static import static
from django.urls import path

from catalog import views
from techline import settings

urlpatterns = [
    path('', views.index)
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# В режиме отладки, то есть DEBUG=TRUE, к urlpatterns добавляется еще один маршрут
# Для статических данных, графических данных указываем сначала settings.MEDIA_URL,
# а затем корневую папку settings.MEDIA_ROOT где будут находится файлы. Все это делается
# только в отладочном режиме