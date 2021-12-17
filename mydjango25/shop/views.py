from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from shop.forms import ReviewForm
from shop.models import Shop, Category, Review


class ShopListView(ListView):
    model = Shop

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["category_list"] = Category.objects.all()
        return context_data


shop_list = ShopListView.as_view(
    model=Shop,
)

shop_detail = DetailView.as_view(
    model=Shop,
)


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    success_url = reverse_lazy("shop:shop_list")

    # 유효성 검사에 통과한다면? 호출되는 form_vaild
    def form_valid(self, form) -> HttpResponse:
        # self.kwargs : URL aptured 값들이 사전으로 저장
        shop_pk = self.kwargs["shop_pk"]
        shop = get_object_or_404(Shop, pk=shop_pk)

        review = form.save(commit=False)
        review.shop = shop
        review.user = self.request.user
        review.save()

        return redirect(shop)

review_new = ReviewCreateView.as_view(
)
