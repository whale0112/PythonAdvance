# INF : 양의 무한대
# -INF : 음의 무한대

def solution(prices):
    INF = 1000000001;
    tmp = INF
    answer = -INF
    for price in prices:
        if tmp != INF:
            answer = max(answer, price - tmp)
        tmp = min(tmp, price)
    return answer

prices1 = [1, 2, 3];
ret1 = solution(prices1);
print("Solution: return value of the function is", ret1, ".")
    
prices2 = [3, 1];
ret2 = solution(prices2);
print("Solution: return value of the function is", ret2, ".")