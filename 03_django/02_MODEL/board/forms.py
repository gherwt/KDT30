# board/forms
from django import forms
from .models import Article
# 1. 입력 데이터 검증 과정 X 
# 2. HTML 만들기 귀찮다

class ArticleForm(forms.ModelForm):
    # 0. 조건이다. (fields에 적힌 컬럼에 대해서만) 
    # 1. 입력 데이터 검증 -> 저장
    # 2. HTML(input/textarea/....)을 생성

    class Meta:
        model = Article
        fields = '__all__'
        # fiedls = ('title',)

