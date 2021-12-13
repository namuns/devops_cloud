from django.contrib import admin

from shop.forms import ShopForm
from shop.models import Shop, Category, Tag


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    form = ShopForm


@admin.register(Category)
class ShopAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

