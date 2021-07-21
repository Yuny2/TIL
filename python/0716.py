#0 import 항상 최상단에 작성을 하자
import requests
from requests.models import Response

# 1. URL에 파이썬으로 요청
url = 'https://www.metaweather.com/api/location/1132599'

# Json 형식을 파이썬 자료구조 변형(.json())
result = requests.get(url).json()
print(result)

# 3. 원하는 값을 추출
print(result['consolidated_weather'])
print(type(result['consolidated_weather'])) #자료구조 파악이 잘 안되면 하나하나 찍어보자 

# 4. 첫번째 데이터 
print(type(result['consolidated_weather'][0]))

day1 = result['consolidated_weather'][0]

print(f'최고기온은 {day1["max_temp"]}')

print(f'''{day1['applicable_date']} : {day["weather_state_name"]}
최고기온은 {day["max_temp"]}, 최저기온은 {day["min_temp"]}
''') 

# 5. 무엇을 반복해야하는가?
# result['consolidated_weather']!!!
for day in result['consolidated_weather']:
    print(f'''{day1['applicable_date']} : {day["weather_state_name"]}
    최고기온은 {day["max_temp"]}, 최저기온은 {day["min_temp"]}
    ''') 