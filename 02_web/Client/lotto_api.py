import requests

res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1086')
data = res.json()  # res 를 dic 형태로 바꿔준다.

# 로또 번호 6개

numbers = []


numbers =  [data[f'drwtNo{i}'] for i in range(1, 7)]
bonus_no = data['bnusNo']

# 보너스 번호
print(numbers, bonus_no)

# JSON => 개발자 쓰라고 => Web API
# API = Applicaiotn Programming Interface