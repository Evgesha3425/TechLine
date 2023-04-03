from django.contrib import admin
from .models import *


class GoodsAdmin(admin.ModelAdmin):
    list_display = ('id', "title", "photo", "time_update", "is_published")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")


class Good_categoryAdmin(admin.ModelAdmin):
    list_display = ('id', "name")
    list_display = ('id', "name")
    search_fields = ("name", )


admin.site.register(Goods, GoodsAdmin)
admin.site.register(Good_category, Good_categoryAdmin)
# admin.site.register(News)