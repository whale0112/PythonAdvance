def solution(N , M):
    total = 0
    for i in range(N, M + 1, 1):
        if i % 2 == 0:
            total += i * i
            
    return total

N = 4
M = 7
ret  = solution(N, M)
print(ret)