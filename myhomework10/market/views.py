from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from market.models import Post

def index(request):
    return render(request, "market/index.html")

def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()

    return render(request, "market/index.html", {
        "post_list": qs,
    })


def post_detail(request: HttpRequest) -> HttpResponse:
    pk = 1
    post = Post.objects.get(pk=pk)
    return render(request, "market/post_detail.html", {
        "post": post,
    })
