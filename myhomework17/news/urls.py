from django.shortcuts import redirect
from django.urls import path

from news import views
from . import views

app_name = "news"

def root(request):
    return redirect("news:news_list")

urlpatterns = [
    path("", views.news_list, name="news_list"),
    path("<int:pk>/", views.news_detail, name="news_detail"),
    path('', root, name="root"),
]

