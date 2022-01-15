import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'

#요청을 보내서, 문서 받아오기
response=requests.get(url)
doc=response.text

#구조 파악 parsing(해석)
data = BeautifulSoup(doc, 'html.parser')

#필요한 데이터 뽑아오기
result = data.select_one('#KOSPI_now')

#데이터 출력
print(result.text)

# 요청(request) -> url
# 응답(response) -> 문서 1장

# url 요청을 보내고, 문서를 달라하는 프로그램 -> client
# url 요청이 오면, 문서를 한장 주는 프로그램 -> server