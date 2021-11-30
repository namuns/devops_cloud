from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def shop_list(request: HttpRequest) -> HttpResponse:
    return render(request, "shop/shop_list.html")