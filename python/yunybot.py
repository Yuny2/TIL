# 텔레그램으로 메시지 보내기
import requests
'''
1. 사용자 정보 가져오기
base_url/getUpdates로 요청 보내서,
chat_id에 해당하는 값을 저장

'''
# 정보
TOKEN = '1675847225:AAGIJ-Lp8wzBOueAktcD6UmHv_Rtwa3vv90'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}'
# url = 
get_updates_url = f'{BASE_URL}/getUpdates'
response = requests.get(get_updates_url).json()
chat_id = response['result'][0]['message']['chat']['id']
# chat_id = 고정된 값 넣어도 된다. 

# 1. 사용자 정보 가져오기
# base_url/getUpdates로 요청 보내서

'''
# 2. 메시지 보내기
# base_url/sendMessage?chat_id={위에서가져온값}&text={원하는 값}
# 메시지 보내기

'''
# 0 . 메시지 준비

import random

magic_number =random.sample(range(1, 46), 6)


text = '안녕하세요?'
send_message_url = f'{BASE_URL}/snedMessage?chat_id={chat_id}&text={text}'

# 1. 요청
requests.get(send_message_url)