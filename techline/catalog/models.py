from django.db import models

# Create your models here.
class Goods(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)  # blank=True - поле может быть пустым
    category = models.SlugField(max_length=20)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')  # upload_to - путь, куда будем сохранять фото, также нужно настроить MEDIA_ROOT и MEDIA_URL
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
