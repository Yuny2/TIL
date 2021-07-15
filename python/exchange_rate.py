# 0. requests 패키지를 가져온다.
import requests
from bs4 import BeautifulSoup

# 1. url을 준비한다.
url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%ED%99%98%EC%9C%A8&oquery=%ED%99%98%EC%9C%A8%EC%A0%95%EB%B3%B4&tqi=hM%2FSulp0YiRsstTC%2Fo4ssssstbK-005612'

# 2. 파이썬으로 요청을 보낸다.
response = requests.get(url).text
# print(response)

# 3. 텍스트에서 정보를 추출한다.
# 정보 추출을 위해서 BuautifulSoup으로 문서 구조화
data = BeautifulSoup(response, 'html.parser')
# 4. 선택지를 활용해서 해당 위치를 찾고
rate = data.select_one('#blind')
# 5. 내용을 출력한다.
print(rate.text)