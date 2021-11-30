from django.db import models
from shop.upload_to import uuid_name_upload_to

class Shop(models.Model):
    Shop_title = models.CharField(max_length=200, verbose_name="제목")
    cartegory = (
        ("생활가전", "생활가전"),
        ("디지털기기", "디지털기기"),
        ("여성의류", "여성의류"),
        ("남성의류", "남성의류"),
    )
    Shop_cartegory = models.CharField(
        max_length=10, choices=cartegory, verbose_name="카테고리", default=""
    )
    Shop_author_name = models.CharField(max_length=20, verbose_name="작성자")
    Shop_price = models.IntegerField(default=0, verbose_name="가격")
    Shop_content = models.TextField(verbose_name="본문")
    # upload_to에 문자열을 지정하면 파일이 저장되는 폴더의 경로가 된다.(파일 많을경우)
    Shop_photo = models.ImageField(blank=True, verbose_name="사진", upload_to=uuid_name_upload_to)
    Shop_created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성시간") # 생성시각
    Shop_updated_at = models.DateTimeField(auto_now=True)
