from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from shop.models import Shop


def shop_list(request: HttpRequest) -> HttpResponse:
    return render(request, "shop/shop_list.html")

    qs = Shop.objects.all() #QuerySet Tyoe
    qs = qs.order_by("-pk")

    q = request.GET.get("q", "")
    if q:
        qs = qs.filter(title__icontains=q)


    return render(request, "shop/shop_list.html", {
        "shop_list": qs,
    })

def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    # pk = 1
    shop = Shop.objects.get(pk=pk) # id도 가능
    return render(request, "shop/shop_detail.html", {
        "shop": shop,
    })