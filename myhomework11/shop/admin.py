from django.contrib import admin
from shop.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["Shop_title", "Shop_author_name", "Shop_price", "Shop_created_at"]
    search_fields = ["Shop_title"]


admin.site.register(Post, PostAdmin)
