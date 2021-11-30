from django.db import models

class Post(models.Model):
    Post_title = models.CharField(max_length=200, verbose_name="제목")
    cartegory = (
        ("생활가전", "생활가전"),
        ("디지털기기", "디지털기기"),
        ("여성의류", "여성의류"),
        ("남성의류", "남성의류"),
    )
    Post_cartegory = models.CharField(
        max_length=10, choices=cartegory, verbose_name="카테고리", default=""
    )
    Post_author_name = models.CharField(max_length=20, verbose_name="작성자")
    Post_price = models.IntegerField(default=0, verbose_name="가격")
    Post_content = models.TextField(verbose_name="본문")
    Post_photo = models.ImageField(blank=True, verbose_name="사진")
    Post_created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성시간") # 생성시각
    Post_updated_at = models.DateTimeField(auto_now=True)