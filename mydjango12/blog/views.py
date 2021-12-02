from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from blog.models import Post


def index(request):
    return render(request, "shop/index.html")


def post_list(request: HttpRequest) -> HttpResponse:
#    request.GET # QueryString Values
#    request.POST # Post 요청 Value
#    request.FILES # Post 요청에서 파일 value

    qs = Post.objects.all() #QuerySet Tyoe
    qs = qs.order_by("-pk")

    #request.GET은 쿼리의 값이 사전으로 저장 q는 검색누르면 주소창에 뜨는 ?q=검색어
    q = request.GET.get("q", "")
    if q:
        qs = qs.filter(title__icontains=q) #i는 ignore이다. 대소문자 구별하나 안하나

   # blog/templates/blog/post_list.html
    return render(request, "blog/post_list.html", {
        "post_list": qs,
    })

def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    # pk = 1
    post = Post.objects.get(pk=pk) # id도 가능
    return render(request, "blog/post_detail.html", {
        "post": post,
    })
