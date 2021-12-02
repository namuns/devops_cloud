from django.db import models


class Order(models.Model):
    #name, address, mobile, menu
    name = models.CharField(max_length=100, verbose_name="이름")
    address = models.CharField(max_length=100, verbose_name="주소")
    mobile = models.CharField(max_length=11, verbose_name="연락처")
    product = models.TextField(max_length=100, verbose_name="주문 상품들") # FK키를 쓰는게 적절
