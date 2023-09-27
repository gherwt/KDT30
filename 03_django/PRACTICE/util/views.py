from django.shortcuts import render
from datetime   import datetime
import requests
from bs4 import BeautifulSoup
import json

def index(request):
    return render(request, 'util/index.html')


def time(request):

    now = datetime.now()

    return render(request, 'util/time.html', {
        'now' : now
    })

def lotto_in(request):

    return render(request,'util/lotto_in.html')


def lotto_out(request):
    
    my = []
    real = []

    res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1086')
    data = res.json()
    
    for i in range(1, 7):
        num = request.GET[f'no{i}']
        real.append(int(data[f'drwtNo{i}']))
        my.append(int(num))

    bonus = int(data['bnusNo'])
    count = 0
    
    count = len(set(my)&set(real))
    if count == 6:
        result = '1등입니다.'

    elif count == 5:
        if bonus in my:
            result = '2등입니다.'
        else:
            result = '3등입니다.'

    elif count == 4:
        result = '4등입니다.'

    elif count == 3:
        result = '5등입니다.'

    else:
        result = '당첨되지 않으셨습니다.'

    return render(request, 'util/lotto_out.html',{  
        'my' : result ,
        'real' : result ,
        'result' : result ,
    })

