# board/forms
from django import forms
from .models import Article, Comment

# 0. 조건이다. (fields에 적힌 컬럼에 대해서만) 
# 1. 입력 데이터 검증 -> 저장
# 2. HTML(input/textarea/....)을 생성
class ArticleForm(forms.ModelForm):
    # django 에서 문자열을 검증할 필드
    # 검증식을 상세하게 설정해줄 수 있다.
    title = forms.CharField(min_length=2, max_length=40)
    content = forms.CharField(
        min_length=5,
        # fomr.charfield 는 기본값이 input type 이다.
        # widget을 통해 HTML 코드도 바꿀 수 있다.
        widget=forms.Textarea(
            # class 주는 코드 예시
            attrs={'class' : 'my-class'}
        )
    )
    class Meta:
        model = Article
        # fiedls = ('content',)
        exclude = ('user', )

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('content',)
        # exclude = ('user', 'article_id')