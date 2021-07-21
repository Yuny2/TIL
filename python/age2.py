'''
tak, tony, eric, musk
4명의 나이를 확인하는 코드
'''
# requests
# import requests
# 1. url 만들어서 요청 보냄
# url = 'https://api.agify.io?name=michael'
# response = request(url).text
# 2. 결과 json을 변환
# result = response.json()
# response = requests.get(url).json()
# print(response['age'])

# 3. 딕셔너리 구조에서 원하는 값만 출력

import requests
# name = input('영문 이름 입력: ')
names = ['tak', 'tony', 'eric', 'musk']
# url = f'https://api.agify.io?name={name}&country_id=KR'
url = 'https://api.agify.io?'
for name in names:
    url += f'name[]={name}&'
responses = requests.get(url).json()  # json() -> dict 형식으로 변환
for response in responses:
    age = response.get('age')
    name = response.get('name')
    print(name, age)