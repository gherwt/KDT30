from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_POST, require_http_methods
from django.contrib.auth.decorators import login_required
from .models import Article, Comment 
from .forms import ArticleForm, CommentForm


# 요청 -> WHERE(=URL), HOW(=METHOD)
# Where => /board/create/
# How => POST, GET 의 차이로 같은 URL 에서 다른 동작을 할 수 있는 것임.
@login_required
@require_http_methods(['GET', 'POST'])
def create(request): 

    if request.method == 'GET':
        form = ArticleForm()

    elif request.method == 'POST':
        form = ArticleForm(data=request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('board:detail', article.pk)
        
    return render(request, 'board/form.html', {
        'form' : form,
        })
 
# read
@require_safe
def index(request):
    # 모든 게시물 조회
    articles = Article.objects.all()

    return render(request, 'board/index.html', {
        'articles' : articles,
    })


@require_safe
def detail(request, pk):
    # article = Article.objects.get(pk=pk)
    article = get_object_or_404(Article, pk=pk)
    # 댓글 작성 HTML
    form = CommentForm()
    comments = article.comment_set.all()

    return render(request, 'board/detail.html', {
        'article' : article,
        'form' : form, 
        'comments' : comments
    })


# update
@login_required
@require_http_methods(['GET', 'POST'])
def edit(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    if request.user != article.user:
        return redirect('board:index', )

    if request.method == 'GET':
        form = ArticleForm(instance = article)

    elif request.method == 'POST': 
        form = ArticleForm(data=request.POST, instance = article) 
        if form.is_valid():
            article = form.save()
            return redirect('board:detail', article.pk)
        
    return render(request, 'board/form.html', {
        'form' : form,
    })

# url 에서 update 를 지우고 edit 만 살리고
# detail 에서 update 를 edit 으로
# delete - POST 요청을 보내야한다. DB에 영향을 미치기 때문임.
@login_required
@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    if request.user != article.user:
        return redirect('board:index', )
    
    article.delete()
    return redirect('board:index')

# URL에서 Delete 를 입력하면 GET 방식으로 지워진다.
# 따로 설정해줘야 Delete 가 발생하지 않는다.


# comment 관련
login_required
@require_POST
def create_comment(request, pk):
    # 게시글을 찾아서 댓글을 나타내는 것이기 때문에 article 을 가져와줘야 한다.
    article = get_object_or_404(Article, pk=pk)
    form = CommentForm(data=request.POST)
    if form.is_valid:
        comment = form.save(commit=False)
        comment.article_id = article
        comment.user = request.user
        comment.save()
    return redirect('board:detail', article.pk)


login_required
@require_POST
def delete_comment(request, pk, comment_pk):
    article = get_object_or_404(Article, pk=pk)
    comment = get_object_or_404(Comment, pk = comment_pk)

    if request.user != comment.user:
        return redirect('board:index', )

    comment.delete()
    return redirect('board:detail', article.pk)