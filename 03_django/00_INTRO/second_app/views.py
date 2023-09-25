from django.shortcuts import render
from datetime import datetime
# Create your views here.

# fibo 는 피보나치 수열 10개를 사용자에게 보여줌
def fibo(request):
    fibo_numbers = [1, 1]

    for _ in range(8):
        x, y = fibo_numbers[-1], fibo_numbers[-2]
        fibo_numbers.append(x+y)        

    return render(request, 'fibo.html', {
        'message' : '피보나치 수열입니다.',
        'fibo_numbers' : fibo_numbers,
    })

# is_xmas 함수는 오늘이 크리스마스라면 yes 아니라면 no
def is_xmas(request):
    today = datetime.now()
    checker = datetime(2023, 12, 25)
    
    result = 'YES' if today.month == checker.month and today.day == checker.day else 'NO'
 
    return render(request, 'is_xmas.html', {
        'today' : '오늘은???',
        'result' : result,
    })