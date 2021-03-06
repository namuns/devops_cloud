from django.core.validators import RegexValidator
from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Shop(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="blog/post/%Y/%m/%d")
    telephone = models.CharField(
        max_length=14,
        validators=[
            RegexValidator(
                r"^\d{3,4}-?\d{3,4}-?\d{4}$"
            )
        ]
    )
    tag_set = models.ManyToManyField("Tag", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]


class Comment(TimeStampedModel):
    post = models.ForeignKey(Shop, on_delete=models.CASCADE)
    message = models.TextField()

    class Meta:
        ordering = ["-id"]
        verbose_name = "댓글"
        verbose_name_plural = "댓글 목록"


class Tag(TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그 목록"
        ordering = ["name"]