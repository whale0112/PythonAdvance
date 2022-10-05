# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(phrases, second):
    a = second % 15
    if a == 0:
        return '_' * 14

    return '_' * (14 - a) + phrases[0:a]

phrases = "happy-birthday"
second = 3
ret = solution(phrases, second)
print("solution 함수의 반환 값은", ret, "입니다.")