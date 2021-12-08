from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class News(TimestampedModel):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()
    photo = models.ImageField(upload_to="news/post/%Y/%m/%d")
    tag_set = models.ManyToManyField("Tag", blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "뉴스"
        verbose_name_plural = "뉴스 목록"


class Comment(TimestampedModel):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=20)
    message = models.TextField()

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "댓글 목록"

class Tag(TimestampedModel):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self) -> str:
        return self.name
