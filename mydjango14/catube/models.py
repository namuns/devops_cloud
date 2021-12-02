from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # 향후 ToDo: 업로드되는 파일이 비디오파일인지 여부를 검사하면 좋다
    video_file = models.FileField()
    thumbnail_file = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
