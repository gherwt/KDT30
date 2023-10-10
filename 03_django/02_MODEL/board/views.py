from django.shortcuts import render, redirect

from .models import Article 
from .forms import ArticleForm

# Create
def new(request):
    form = ArticleForm() # input tag 를 대신 생성
    return render(request, 'board/new.html', {
        'form' : form,
    }) 

def create(request):

    # 데이터 입력
    form = ArticleForm(data=request.POST)
    
    # 데이터 검증 

    # 유효한 데이터라면,
    if form.is_valid():
        # validation -> 유효성 검증// is_(T or F return)
        # 저장
        article = form.save()
        return redirect('board:detail', article.pk)
    
    # 유효하지 않은 데이터라면,
    else:
        return render(request, 'board/new.html', {
            'form' : form,
        })
 
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
    form = ArticleForm(instance = article)

    return render(request, 'board/edit.html', {
        'article' : article,
        'form' : form,
    })


def update(request, pk):

    article = Article.objects.get(pk=pk)
    # 기존에 있는 data 를 가져온다.
    form = ArticleForm(data=request.POST, instance = article)
    
    # 데이터 검증 

    # 유효한 데이터라면,
    if form.is_valid():
        # validation -> 유효성 검증// is_(T or F return)
        # 저장
        article = form.save()
        return redirect('board:detail', article.pk)
    
    # 유효하지 않은 데이터라면,
    else:
        return render(request, 'board/edit.html', {
            'article' : article,
            'form' : form,
        })
 

# delete
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('board:index')