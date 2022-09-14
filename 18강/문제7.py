def solution(num):
    num += 1
    digit = 1
    while num //  digit % 10 == 0:
        num += digit
        digit *= 10
    return num

num = 9949999;
ret = solution(num)
print("Solution: return value of the function is", ret, ".")