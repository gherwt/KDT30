from django.shortcuts import render, redirect

from .models import Student
# 현재 폴더 내의 form 파일에서 Studentfrom 을 가져온다
from .forms import StudentForm


def new(request):
    # form 에서 StudentForm 을 가져와준다.
    form = StudentForm()

    # form 에서 data 를 가져오기 때문에 dict 설정해준다.
    return render(request, 'crud/new.html',{
        'form' : form,
    })

def create(request):
    # new.html 에서 Post 한 data 를 가져와 저장한다.
    form = StudentForm(data = request.POST)

    # 유효성 검사를 실시, 데이터를 잘 입력했는지 확인한다.
    if form.is_valid():
        student = form.save() # 저장됨 => id(pk)가 생긴다.
        # 저장한 Data 를 보여준다.
        return redirect('crud:detail', student.pk)
    
    # 유효하지 않으면 다시 new.html 을 보여준다.
    else:
        return render(request, 'crud/new.html', {
            'form' : form
        })
    
def index(request):
    # 전체 학생 목록 확인하기
    students = Student.objects.all()

    return render(request, 'crud/index.html', {
        'students' : students,
    })

def detail(request, pk):
    # 특정 학생의 상세 정보를 확인
    student = Student.objects.get(pk=pk) 

    return render(request, 'crud/detail.html', {
        'student' : student,
    })

def edit(request, pk):
    # student 를 수정하기 위한 <form> => 작성 데이터는 update 로 보내준다.
    student = Student.objects.get(pk=pk)

    # form 에서 특정 학생 정보를 가져온다.
    form = StudentForm(instance = student)   

    # edit.html로 보내줘서 작업을 한다.
    # student, form data 2 가지를 받아줘야 하므로 2개를 dict 설정해준다.
    return render(request, 'crud/edit.html', {
        'student' : student,
        'form' : form,
    })

def update(request, pk):
    # edit 에서 자료를 받아온다. 그리고 저장한다.
    student = Student.objects.get(pk=pk)
    form = StudentForm(data = request.POST, instance = student)   
    

    # create 와 마찬가지로 input 한 data 의 유효성 검사를 실시해준다.
    if form.is_valid():
        student = form.save()
        return redirect('crud:detail', student.pk)
    
    # 유효하지 않으면 다시 수정하기 위해 edit 를 열어준다.
    else:
        return render('crud/edit.html',student.pk, {
            'form' : form,
            'student' : student,
        })

def delete(request, pk):
    # URL 에 넘어온 pk 에 해당하는 학생정보를 삭제한다.
    student = Student.objects.get(pk=pk)
    student.delete()
    
    return redirect('crud:index')
    # DTL(템플릿) {% url "crud:index" %}
    # view 에서 redirect -> "crud:index" 이렇게 쓰면 된다.