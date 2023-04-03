from django.db import models
from django.urls import reverse


class Goods(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name="Фото")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    cat = models.ForeignKey('Good_category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('good', kwargs={'good_id': self.pk})

    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = "Товары"
        ordering = ["time_update", "title"]


class Good_category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name="Название")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["id"]



# class News(models.Model):
#     news_name = models.CharField(max_length=100)
#     content = models.TextField(help_text="Введите текст новости")  # blank=True - поле может быть пустым
#     category = models.SlugField(max_length=20)
#     photo = models.ImageField(upload_to='images/%Y/%m/%d/')  # upload_to - путь, куда будем сохранять фото, также нужно настроить MEDIA_ROOT и MEDIA_URL
#     time_create = models.DateTimeField(auto_now_add=True)
#     time_update = models.DateTimeField(auto_now=True)
#     is_published = models.BooleanField(default=True)
#
#     def __str__(self):
#         return self.news_name
#
#     class Meta:
#         ordering = ["is_published"]
#         verbose_name = "Новости"