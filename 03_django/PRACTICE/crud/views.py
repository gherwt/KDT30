from django.shortcuts import render, redirect, get_object_or_404

from django.views.decorators.http import require_http_methods, require_POST, require_safe
# 현재 폴더 내의 form 파일에서 Studentfrom 을 가져온다
from .models import Student
from .forms import StudentForm

@require_http_methods(['GET', 'POST'])
def new(request):
    if request.method == 'GET':
        form = StudentForm()
    
    elif request.method == 'POST':
        form = StudentForm(data = request.POST)
        if form.is_valid():
            student = form.save() 
            return redirect('crud:detail', student.pk)
        
    return render(request, 'crud/form.html', {
        'form' : form
        })
       
@require_safe    
def index(request):
    # 전체 학생 목록 확인하기
    students = Student.objects.all()
    return render(request, 'crud/index.html', {
        'students' : students,
    })

@require_safe    
def detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'crud/detail.html', {
        'student' : student,
    })

@require_http_methods(['GET', 'POST'])
def update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    
    if request.method == 'GET':
        form = StudentForm(instance = student)   

    elif request.method == 'POST':
        form = StudentForm(data=request.POST, instance = student)  
        if form.is_valid():
            student = form.save()
            return redirect('crud:detail', student.pk)
        
    return render(request, 'crud/form.html', {
        'form' : form,
        })

@require_POST
def delete(request, pk):
    # URL 에 넘어온 pk 에 해당하는 학생정보를 삭제한다.
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('crud:index')
    # DTL(템플릿) {% url "crud:index" %}
    # view 에서 redirect -> "crud:index" 이렇게 쓰면 된다.