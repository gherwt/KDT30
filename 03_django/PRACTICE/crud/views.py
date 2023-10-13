from django.shortcuts import render, redirect, get_object_or_404

from django.views.decorators.http import require_http_methods, require_POST, require_safe
# 현재 폴더 내의 form 파일에서 Studentfrom 을 가져온다
from django.contrib.auth.decorators import login_required
from .models import Student, Reply
from .forms import StudentForm, ReplyForm

# login 이 되어 있어야만 실행되게 하는 decorators 이다.
@login_required
@require_http_methods(['GET', 'POST'])
def new(request):
    # 유저가 로그인 되어 있을 때 상세페이지를 나타나게 한다.
    if request.user_is_authedicated:
        return redirect('crud:detail', student.pk)

    if request.method == 'GET':
        form = StudentForm()
    
    elif request.method == 'POST':
        form = StudentForm(data = request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            # student를 작성한 user 가 요청한 user 인지를 확인
            student.user = request.user
            form.save()
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


@login_required
@require_safe    
def detail(request, pk):
    # student 값이 맞으면 불러오고 아니면 404 error 가 뜬다.
    student = get_object_or_404(Student, pk=pk)

    # Reply 를 작성할 수 있는 Form 을 불러와준다.
    form = ReplyForm()

    # stundent 에서 reply를 역참조한다(1에서 n 값을 가져온다.)
    replys = student.reply_set.all()

    return render(request, 'crud/detail.html', {
        'student' : student,
        'form' : form,
        'replys' : replys,
    })


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    
    # 요청한 유저, 현재 로그인 되어 있는 유저가 student 를 작성한 유저가 아닐 경우
    if request.user != student.user:
        # 메인 페이지를 보여준다.
        return redirect('crud:index',)
    
    # get 요청이면 form 을 보여준다.
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


@login_required
@require_POST
def delete(request, pk):
    # URL 에 넘어온 pk 에 해당하는 학생정보를 삭제한다.
    student = get_object_or_404(Student, pk=pk)
    
    # 요청한 유저가 student 를 작성한 유저가 아니라면 삭제할 수 없다.
    if request.user != student.user:
        return redirect('crud:index',)
    
    student.delete()
    return redirect('crud:index')
    # DTL(템플릿) {% url "crud:index" %}
    # view 에서 redirect -> "crud:index" 이렇게 쓰면 된다.

@login_required
def reply_create(request, pk):
    # 댓글 작성을 위해서 일단 게시물에 연결해줘야 하기 때문에 student.pk 가 필요하다.
    student = get_object_or_404(Student, pk=pk)
    # 나타낼 form (틀)은 Reply model 을 바탕으로 작성한 ReplyForm 이다.
    form =  ReplyForm(data= request.POST)
    
    # form 에 입력한 데이터가 유효할 경우
    if form.is_valid():
        # reply 를 실행, form 을 저장한다. 하지만 그 전에 확인 작업을 실시한다.
        reply = form.save(commit=False)
        # student 의 pk 에 univ 가 저장되기 때문에 Reply에 저장될 student 의 pk 값이 student 에 저장되어져 있는 pk 값과 동일한 지를 확인해준다.
        reply.student = student
        # 작성자와 요청자가 동일한지를 확인한다.
        reply.user = request.user
        # 이제 저장해준다.
        reply.save()

    return redirect('crud:detail', student.pk)
        

@login_required
def reply_delete(request, pk, reply_pk):
    # 작성된 글의 pk 값이 필요
    student = get_object_or_404(Student, pk=pk)
    # 글에 작성되어져 있는 univ 의 reply 값이 필요하다.
    reply = get_object_or_404(Reply, pk = reply_pk)

    # 만약 요청 유저와 작성 유저가 다르다면
    if request.user != reply.user:
        # detail 창을 보여주고
        return redirect('crud:detail', )
    
    # reply 를 삭제한다.

    reply.delete()
    # 해당 글을 다시 불러들여온다.
    return redirect('crud:detail', student.pk)

