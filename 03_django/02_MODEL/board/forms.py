# board/forms
from django import forms
from .models import Article

# 0. 조건이다. (fields에 적힌 컬럼에 대해서만) 
# 1. 입력 데이터 검증 -> 저장
# 2. HTML(input/textarea/....)을 생성
class ArticleForm(forms.ModelForm):
    
    # django 에서 문자열을 검증할 필드
    title = forms.CharField(min_length=2)
    content = forms.CharField(min_length=5)


    class Meta:
        model = Article
        fields = '__all__'
        # fiedls = ('title',)

