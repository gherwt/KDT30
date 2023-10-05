from django.shortcuts import render

# Create your views here.

def new(request):
    pass
    return render(request, 'board/new.html')

def index(request):
    pass
    return render(request, 'board/.html')

def create(request):
    pass
    return render(request, 'board/create.html')

def detail(request, pk):
    pass
    return render(request, 'board/<int:pk>.html',{
        'pk' : pk
    })

def edit(request):
    pass
    return render(request, 'board/edit.html')

def update(request):
    pass
    return render(request, 'board/update.html')

def delete(request):
    pass
    return render(request, 'board/delete.html')