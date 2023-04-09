from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', "title", "photo", "price", "balance","time_update", "is_published", "category")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")

    def get_photo_url(self, object):
        if object.photo:
            return mark_safe(f"")


class Good_categoryAdmin(admin.ModelAdmin):
    list_display = ('id', "name")
    list_display = ('id', "name")
    search_fields = ("name", )


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Good_category, Good_categoryAdmin)
# admin.site.register(News)