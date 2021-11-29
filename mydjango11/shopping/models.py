from django.db import models

from django.db import models


class Item(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="주문 번호")
    client = models.CharField(default=0, max_length=20, verbose_name="주문자 성함")
    item_name = models.CharField(max_length=20, verbose_name="상품명")
    price = models.IntegerField(default=0, verbose_name="가격")
    gift = models.BooleanField(default=0, verbose_name="포장여부")
    gift_date = models.DateTimeField(default=0, verbose_name="원하는 배달 시간")
    deliver = models.TextField(default=0, max_length=120, verbose_name="배송시 요청사항")
    order_date = models.DateTimeField(auto_now_add=True, verbose_name="주문 날짜")

    def __str__(self):
        return self.item_name

