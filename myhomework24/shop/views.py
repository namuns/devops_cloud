from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from shop.forms import ShopForm, CommentForm
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


def shop_detail(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)
    comment_list = shop.comment_set.all()

    return render(request, "shop/shop_detail.html", {
        "shop": shop,
        "comment_list": comment_list,
    })


def shop_edit(request: HttpRequest, pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=pk)

    if request.method == "POST":
        form = ShopForm(request.POST, request.FILES, instance=Shop)

    else:
        form = ShopForm(instance=shop)

    return render(request, "shop/shop_form.html", {
        "form": form,
    })


def comment_new(request: HttpRequest, shop_pk: int) -> HttpResponse:
    shop = get_object_or_404(Shop, pk=shop_pk)

    if request.method == "POST":
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.shop = shop
            comment.save()
            return redirect("shop:post_detail", shop_pk)
    else:
        form = ()

    return render(request, "shop/comment_form.html", {
        "form": form,
    })