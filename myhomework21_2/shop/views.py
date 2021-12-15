from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from shop.forms import ShopForm
from shop.models import Shop, Category


def shop_list(request: HttpRequest) -> HttpResponse:
    category_qs = Category.objects.all()
    qs = Shop.objects.all()


    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(name__icontains=query)


    category_id : str = request.GET.get("category_id", "")
    if category_id:
        qs = qs.filter(category__pk=category_id)

    return render(request, "shop/shop_list.html", {
        "shop_list": qs,
        "category_list": category_qs,

    })


def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)
    tag_list = shop.tag_set.all


    return render(request, "shop/shop_detail.html", {
        "shop": shop,
        "tag_list" : tag_list,
    })


def shop_edit(request: HttpRequest, shop_pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=shop_pk)

    if request.method == "POST":
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            saved_post = form.save()
            return redirect("shop:shop_detail", saved_post.pk)
    else:
        form = ShopForm(instance=shop)

    return render(request, "shop/shop_form.html", {
        "form": form,
    })

