from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from news.models import News


def news_list(request: HttpRequest) -> HttpResponse:
    qs = News.objects.all()

    query = request.GET.get("query", "")
    if query:
        qs = qs.filter(title__icontains=query)

    return render(request, "news/news_list.html", {
        "news_list": qs,
    })

def news_detail(request: HttpRequest, pk: int) -> HttpResponse:
    news = News.objects.get(pk=pk)
    return render(request, "news/news_detail.html", {
        "news": news,
    })