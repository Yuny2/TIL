# 요청 보내주는 requests를 가져온다.
import requests

# 1. url로 요청을 보낸 결과를 저장한다.
url = 'https://api.agify.io?name=michael'
# 저장하는데, 이거 json이라서 리스트-딕셔너리 구조로 바꿔줘!
response = requests.get(url)
# 2. 결과 json을 변환
result = response.json()
print(result)

# print(response)
# print(type(response))
# print(response['age'])
# print('==========')
# 저장하는데, 이거 text로 바꿔줘 -> BeautifulSoup으로 구조화(HTML) -> 선택자
# response_text = requests.get(url).text
# print(response_text)
# print(type(response_text))