from django.urls import path

from shop import views

urlpatterns = [
    path("", views.shop_list, name="shop_list"),
]