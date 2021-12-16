from django.urls import path

from shop import views

app_name ="shop"

urlpatterns = [
    path("", views.shop_list, name="shop_list"),
    path("new/", views.shop_new, name="shop_new"),
    path("<int:pk>/", views.shop_detail, name="shop_detail"),
    path("<int:pk>/edit", views.shop_edit, name="shop_edit"),
    path("<int:shop_pk>/comment/new/", views.comment_new, name="comment_new"),
    path("<int:shop_pk>/comment/<int:pk>/edit", views.comment_edit, name="comment_edit"),
    path("tag/<str:shop_pk>/", views.tag_detail, name="tag_detail"),

]