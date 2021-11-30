from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from market.models import Post

def index(request):
    return render(request, "market/index.html")

def post_list(request: HttpRequest) -> HttpResponse:

    return render(request, "market/index.html")