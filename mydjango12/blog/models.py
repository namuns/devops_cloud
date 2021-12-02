from django.db import models
from blog.upload_to import uuid_name_upload_to

class Post(models.Model):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    content = models.TextField()
    # upload_to에 문자열을 지정하면 파일이 저장되는 폴더의 경로가 된다.(파일 많을경우)
    photo = models.ImageField(blank=True, upload_to=uuid_name_upload_to)# upload_to='shop/post/%Y/%m/%d/%H')
    created_at = models.DateTimeField(auto_now_add=True) # 생성시각(nowadd생성시 자동생성)
    updated_at = models.DateTimeField(auto_now=True) # add없으면..
