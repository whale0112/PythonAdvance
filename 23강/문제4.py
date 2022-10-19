# 다음과 같이 import를 사용할 수 있습니다.
# import math
def func_a(l1, l2):
    count = 0
    for i in range(len(l1)-1, 0, -1):
        if l1[i:len(l1)] == l2[0:i+1]:
            if len(l1[i:len(l1)]) >= count:
                count = len(l1[i:len(l1)])
    answer = len(l1) + len(l2) - count
    return answer
    

def solution(s1, s2):
    answer = 0
    l1 = list(s1)
    l2 = list(s2)
    answer = min(func_a(l1, l2), func_a(l2, l1))
    return answer

s1 = "ababc"
s2 = "abcdab"
ret = solution(s1, s2)
print("solution 함수의 반환 값은", ret, "입니다.")
