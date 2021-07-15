# 로또 번호 6개 추첨하는 코드 작성하기
# 코드 실행은 python 파일명.py
# 1. random 모듈을 가져오고
import random
# 2. numbers 통을 만들고
numbers = range(1,46)
# 3. random 에서 sample을 6개 하고, pick에 저장하고
pick = random.sample(numbers,6)
# 4. pick 출력
print(pick)