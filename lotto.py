# random 모듈을 꺼낸다
import random

# 1 ~ 45 까지의 숫자가 들어있는 통을 만든다
numbers = range(1,46)

# 통에서 6개를 랜덤으로 고른다.
lucky = random.sample(numbers, 6) # samples는 입력된 숫자만큼 랜덤으로 추출 

# 고른 숫자를 출력
print(lucky)
