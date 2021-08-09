from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

# Create your models here.
class Blog(models.Model):
    latitude = models.FloatField(default=0.0) #위도
    longitude = models.FloatField(default=0.0) #경도
    hashtag = models.TextField(max_length=20) #해시태그는 하나만 적을 수 있도록 하는 게 편할듯
    weather = models.TextField() #4개로 구분 - cloudy, sunny, rainy, snowy
    images = models.ImageField(upload_to ="images", blank = True, null = True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE )#작성자 여기 수정
    created_at = models.DateTimeField(auto_now_add=True) #작성시각
    #pub_date = models.DateTimeField('data published')
    body = models.TextField(max_length=200) #글 본문

    def __str__(self):
        return str(self.latitude) + ", " + str(self.longitude) #일단 위도, 경도 표시하도록 해놓음 ->편의에 따라 바꿔도 ㄱㅊ

class Comment(models.Model):
  post = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)
  body = models.TextField()
  date = models.DateTimeField(default=timezone.now)