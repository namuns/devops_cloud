from django.urls import path

from shop import views

app_name ="shop"

urlpatterns = [
    path("", views.shop_list, name="shop_list"),
    path("new/", views.shop_new, name="shop_new"),
]