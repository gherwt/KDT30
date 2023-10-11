from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    # 여기에 검증식을 추가 설정해줄 수 있다.
    # 파이썬 코드로 설정해주는 것이라고 보면 됨
    class Meta:
        model = Student
        fields = '__all__'