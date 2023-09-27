
# requests 는 client 이다.

import requests
from bs4 import BeautifulSoup

# Crawling

# 요청 => 응답 객체
res = requests.get('https://finance.naver.com/sise/')

# HTML 문서 파싱 완료 결과
soup = BeautifulSoup(res.text, 'html.parser')

# KOSPI_now 를 가져오는 방법

# naver.select('#KOSPI_now')
# naver.select_one('#KOSPI_now')
# naver.find(id = 'KOSPI_now')

KOSPI_tag = soup.select_one('#KOSPI_now')
KOSDAQ_tag = soup.select_one('#KOSDAQ_now')

print(KOSPI_tag.text)