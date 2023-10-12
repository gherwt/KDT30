from django.contrib import admin
from .models import Article


# admin 계정에서 board 설정하기

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    
    list_display = ['id', 'title', 'created_at']
    list_display_links = ['title']

