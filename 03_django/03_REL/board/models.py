from django.db import models

# Create your models here.

# 데이터 타입만 나타낸다.
class Article(models.Model):
    # SQL) VARCHAR
    title = models.CharField(max_length=200)
    # SQL) TEXT
    content = models.TextField()
    # Timestamp => 생성시간/수정시간
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
