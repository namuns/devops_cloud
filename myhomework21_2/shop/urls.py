from django.urls import path
from shop import views
from shop.views import shop_detail

app_name = "shop"

urlpatterns = [
    path("", views.shop_list, name="shop_list"),
    path("<int:pk>/", shop_detail, name="shop_detail"),
]