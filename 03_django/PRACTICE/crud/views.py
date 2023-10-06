from django.shortcuts import render, redirect
from .models import Student


def new(request):
    # 새로운 student 를 생성하기 위한 form(html) -> 작성 data 는 create 함수로 보내줘야 한다
    return render(request, 'crud/new.html')

def create(request):
    student = Student()
    student.name = request.GET['student_name']
    student.age = request.GET['student_age']
    student.major = request.GET['student_major']
    student.description = request.GET['student_description']
    student.save() # 저장됨 => id(pk)가 생긴다.
    
    return redirect(f'/school/{student.pk}/')

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
    return render(request, 'crud/edit.html', {
        'student' : student,
    })

def update(request, pk):
    # edit 에서 자료를 받아온다. 그리고 저장한다.
    student = Student.objects.get(pk=pk)
    student.name = request.GET['student_name']
    student.age = request.GET['student_age']
    student.major = request.GET['student_major']
    student.description = request.GET['student_description']
    student.save() # 여기서는 저장되면서 id 가 생기지는 않는다.

    return redirect(f'/school/{student.pk}/')

def delete(request, pk):
    # URL 에 넘어온 pk 에 해당하는 학생정보를 삭제한다.
    student = Student.objects.get(pk=pk)
    student.delete()
    
    return redirect('/school/')