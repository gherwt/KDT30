from django.shortcuts import render, redirect
from .models import Article 

# Create
def new(request):
    return render(request, 'board/new.html')

def create(request):

    article = Article()
    article.title = request.GET['title']
    article.content = request.GET['content']
    article.save()
    
    # redirect 강제로 이동시키는 method
    return redirect(f'/board/{article.pk}/')

# read

def index(request):
    # 모든 게시물 조회
    articles = Article.objects.all()
    return render(request, 'board/index.html', {
        'articles' : articles,
    })

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'board/detail.html', {
        'article' : article,
    })

# update
def edit(request, pk):
    article = Article.objects.get(pk=pk)
    return render(request, 'board/edit.html', {
        'article' : article,
    })


def update(request, pk):

    article = Article.objects.get(pk=pk)
    article.title = request.GET['title']
    article.content = request.GET['content']
    article.save()

    return redirect(f'/board/{article.pk}/')

# delete
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('/board/')