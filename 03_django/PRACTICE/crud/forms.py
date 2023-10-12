from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    # 여기에 검증식을 추가 설정해줄 수 있다.
    # 파이썬 코드로 설정해주는 것이라고 보면 됨

    # 상수(값이 초기화/할당 이후 절대 변하면 안된다는 뜻.)
    CHOICES = [
        ('SOC', '사회학'),
        ('POL', '정치외교학'),
        ('CSE', '컴퓨터공학'),
        ('PSY', '심리학'),
        ('BUS', '경영학'),
        ('CHE', '화학공학'),

    ]
    name = forms.CharField(min_length=1, max_length=10)
    age = forms.IntegerField(min_value=10, max_value=200)
    major = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices= CHOICES
    )
    description = forms.CharField(
        widget=forms.Textarea(),
        min_length=5
    )

    class Meta:
        model = Student
        exclude = ('user', )
        fields = '__all__'