from django.contrib import admin

from shop.models import Shop

class ShopAdmin(admin.ModelAdmin):
    list_display = ["Shop_title", "Shop_author_name", "Shop_created_at"]
    search_fields = ["Shop_title"]


admin.site.register(Shop, ShopAdmin)
