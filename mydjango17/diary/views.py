from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from diary.models import Post


def post_list(request: HttpRequest) -> HttpResponse:
    qs = Post.objects.all()
    return render(request, "diary/post_list.html", {
        "post_list": qs,
    })
