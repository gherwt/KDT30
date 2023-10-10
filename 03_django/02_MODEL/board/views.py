from django.shortcuts import render, redirect

from .models import Article 
from .forms import ArticleForm


# 요청 -> WHERE(=URL), HOW(=METHOD)
# Where => /board/create/
# How => POST, GET 의 차이로 같은 URL 에서 다른 동작을 할 수 있는 것임.

# def create(request): 
#     if request.method == 'GET':
#         form = ArticleForm()  input tag 를 대신 생성
#         return render(request, 'board/form.html', {
#                 'form' : form,
#         }) 
    
#     # 데이터 입력
#     elif request.method == 'POST':
#         form = ArticleForm(data=request.POST)
        # 데이터 검증 
        # 유효한 데이터라면,
#         if form.is_valid():
             # validation -> 유효성 검증// is_(T or F return)
             # 저장
#             article = form.save()
#             return redirect('board:detail', article.pk)
        
         # 유효하지 않은 데이터라면,
#         else:
#             return render(request, 'board/form.html', {
#                 'form' : form,
#             })

# 리펙토링 후
def create(request): 
    if request.method == 'GET':
        form = ArticleForm()
    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('board:detail', article.pk)
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


# def update(request, pk):

#     article = Article.objects.get(pk=pk)
     # 기존에 있는 data 를 가져온다.
#     form = ArticleForm(data=request.POST, instance = article)
    
     # 데이터 검증 

     # 유효한 데이터라면,
#     if form.is_valid():
        # validation -> 유효성 검증// is_(T or F return)
        # 저장
#         article = form.save()
#         return redirect('board:detail', article.pk)
    
     # 유효하지 않은 데이터라면,
#     else:
#         return render(request, 'board/form.html', {
#             'article' : article,
#             'form' : form,
#         })
    
# update
def edit(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'GET':
        form = ArticleForm(instance = article)

    elif request.method == 'POST': 
        form = ArticleForm(data=request.POST, instance = article) 
        if form.is_valid():
            article = form.save()
            return redirect('board:detail', article.pk)
        
    return render(request, 'board/edit.html', {
        # 'article' : article,
        'form' : form,
    })
# url 에서 update 를 지우고 edit 만 살리고
# detail 에서 update 를 edit 으로

# delete
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('board:index')