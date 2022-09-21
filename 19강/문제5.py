#다음과 같이 import를 사용할 수 있습니다.
#import math

def solution(arr):
    answer = 0
    count = 1
    for i in range(1, len(arr), 1):
        if arr[i] > arr[i - 1]:
            count += 1
        elif answer < count:
            answer = count
            count = 1
    return answer

arr = [3, 1, 2, 4, 5, 1, 2, 2, 3, 4]
ret = solution(arr)
print("solution 함수의 반환 값은", ret, "입니다.")