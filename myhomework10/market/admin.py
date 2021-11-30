from django.contrib import admin
from market.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ["Post_title", "Post_author_name", "Post_created_at"]
    search_fields = ["Post_title"]


admin.site.register(Post, PostAdmin)