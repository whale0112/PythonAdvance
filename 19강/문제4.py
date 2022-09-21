#다음과 같이 import를 사용할 수 있습니다.
#import math
# TODO 더 효율적으로 바꿔보기

def solution(arr, K):
    answer = 0
    for a in arr:
        for b in arr:
            for c in arr:
                if a != b and b != c and c != a:
                    if (a + b + c) % K == 0:
                        answer += 1
    return answer / 6

arr = [1, 2, 3, 4, 5]
K = 3
ret = solution(arr, K)
print("solution 함수의 반환 값은 ", ret, " 입니다.")