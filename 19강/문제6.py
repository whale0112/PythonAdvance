#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(commands):
    answer = [0, 0]
    for c in commands:
        if c == 'L':
            answer[0] -= 1
        elif c == 'R':
            answer[0] += 1
        elif c == 'U':
            answer[1] += 1
        else:
            answer[1] -= 1
    return answer

commands = "URDDL"
ret = solution(commands)
print("solution 함수의 반환 값은 ", ret, " 입니다.")