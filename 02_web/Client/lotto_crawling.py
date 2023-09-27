import requests
from bs4 import BeautifulSoup


res = requests.get('https://dhlottery.co.kr/common.do?method=main')
soup = BeautifulSoup(res.text, 'html.parser')

# num = soup.select_one('#article > div.wrap_box.wrap1 > section.box.win.win645 > div > p')
# print(num)


# if res.status_code == 200:
#     html = res.text
#     num = soup.select_one('#article > div.wrap_box.wrap1 > section.box.win.win645 > div > p')
#     print(num)
# else : 
#     print(res.status_code)

no1 = soup.select_one('drwtNo1') # 1번 방식

numbers = []

for i in range(1,7):
    num = int(soup.select_one(f'#drwtNo{i}').text)
    numbers.append(num)
print(numbers)

bonus_no = int(soup.select_one('#bnusNo').text)

print(bonus_no)

# HTML => 정보 긁기(scraping) => GUI