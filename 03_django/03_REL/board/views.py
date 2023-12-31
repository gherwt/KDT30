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
    # article 에 request.user 가 좋아요를 눌렀는가???
    comments = article.comment_set.all()
    is_like = article.like_users.filter(pk=request.user.pk).exists()

    return render(request, 'board/detail.html', {
        'article' : article,
        'form' : form, 
        'comments' : comments,
        'is_like': is_like, 
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
@login_required
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


@login_required
@require_POST
def delete_comment(request, pk, comment_pk):
    article = get_object_or_404(Article, pk=pk)
    comment = get_object_or_404(Comment, pk = comment_pk)

    if request.user != comment.user:
        return redirect('board:detail', )

    comment.delete()
    return redirect('board:detail', article.pk)

@login_required
@require_POST
def like(request, pk):
    
    # 모델링 -> view 함수 -> ui/ 시나리오
    # detail 에 버튼 필요 -> 여기 함수에 진입 -> 다시 detail로 리다이렉트
    article = get_object_or_404(Article, pk=pk)
    user = request.user

    # 현재 게시글에 좋아요를 누른 사용자 전체 중에 지금 요청보낸 이가 있다면
    # if user in article.like_users.all(): # Python
    # 게시글에 좋아요가 많을 경우에는 사용자에 대해서 찾는다.
    # if article in user.like_articles():

    if article.like_users.filter(pk=user.pk).exists():
        # 좋아요를 눌랐다면, 좋아요를 취소할 수 있도록 할 수 있게 한다.
        article.like_users.remove(user) 


    # 만약 요청을 보낸 사용자가 기존에 좋아요를 누르지 않았다면,
    else:
        article.like_users.add(user) 
        # user.like_users.add(article) 위, 아래가 같다

    
    return redirect('board:detail', article.pk)