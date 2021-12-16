from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from shop.models import Shop


def shop_list(request: HttpRequest) -> HttpResponse:

    qs = Shop.objects.all()
    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(name__icontains=query)
    return render(request, "shop/shop_list.html", {
        "shop_list": qs,
    })

