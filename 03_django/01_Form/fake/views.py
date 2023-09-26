from django.shortcuts import render

def index(request):
    return render(request, 'fake/index.html')
# Create your views here.
