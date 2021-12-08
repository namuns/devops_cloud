from django.contrib import admin
from news.models import News, Comment, Tag



@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass