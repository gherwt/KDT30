from django.db import models
# from django.conf import settings
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()

# 데이터 타입만 나타낸다.
class Article(models.Model):
    # SQL) VARCHAR
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    # SQL) TEXT
    content = models.TextField()
    # Timestamp => 생성시간/수정시간
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(User, related_name='like_articles')

class Comment(models.Model):

    # 클래스 명은 "" 씌워주지 않아도 된다.
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article_id = models.ForeignKey(Article, on_delete=models.CASCADE)

    content = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)