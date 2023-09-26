from django.shortcuts import render
from datetime   import datetime


def index(request):
    return render(request, 'util/index.html')


def time(request):

    now = datetime.now()

    return render(request, 'util/time.html', {
        'now' : now
    })