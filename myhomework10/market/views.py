from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def post_list(request: HttpRequest) -> HttpResponse:
    return render(request, "market/index.html")