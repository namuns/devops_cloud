from django.urls import path
from shop import views
from shop.views import shop_detail, shop_edit

app_name = "shop"

urlpatterns = [
    path("", views.shop_list, name="shop_list"),
    path("<int:pk>/", shop_detail, name="shop_detail"),
    path("<int:shop_pk>/edit/", shop_edit, name="shop_edit"),
]