from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from shop.forms import ShopForm
from shop.models import Shop


def shop_list(request: HttpRequest) -> HttpResponse:

    qs = Shop.objects.all()
    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(name__icontains=query)
    return render(request, "shop/shop_list.html", {
        "shop_list": qs,
    })

def shop_new(request: HttpRequest) -> HttpResponse:

    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES)
        if form.is_valid():
            saved_post = form.save()
            return redirect("shop:shop_detail", saved_post.pk)
    else:
        form = ShopForm()

    return render(request, "shop/shop_form.html", {
        "form": form,
    })
