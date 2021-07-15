import requests
# name = input('영문 이름 입력: ')
names = ['tak', 'tony', 'eric', 'musk']
# url = https://api.nationalize.io/?name=michael
url = 'https://nationalize.io/?name='
for name in names:
    url = 'https://nationalize.io/?name='
    url += name
    print(url)
responses = requests.get(url).json()  # json() -> dict 형식으로 변환
for response in responses:
    country_id = response.get('country_id')
    name = response.get('name')
    print(name + '의 국가는' + country_id + '입니다.')