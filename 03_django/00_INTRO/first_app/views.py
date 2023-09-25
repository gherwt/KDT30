from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.

# 1. function view
# 2. class view
# 이곳으로 url 파일을 가져오면 url 로는 사용할 수 없다..


def hello(request):
    return render(request, 'a.html')

def bye(request):
    return HttpResponse('Goodbye ~ It is lunch time')

def lotto(request):

    lotto = []
    rnd_num = random.randint(1, 45)
    # randint() 함수를 사용하여 난수를 생성


    for i in range(6): # 번호 6개를 랜덤으로 추출함
        while rnd_num in lotto: # 6개가 될 때까지 반복 실행한다.
            rnd_num = random.randint(1, 45)
        lotto.append(rnd_num) # 난수를 생성하고 빈 리스트에 저장
    lotto.sort() # 중복 여부를 확인한다.

    # lucky_numbers = random.sample(range(1, 46), 6)  이렇게 간단하게도 가능하다.
    # print 로 확인 가능 url 접속을 해서 새로고침을 하면 터미널 창에서 볼 수 있다.
    return HttpResponse([lotto])