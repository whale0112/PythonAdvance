from multiprocessing.connection import answer_challenge


def func_a(arr): #3의 배수 숫자
    count = 0
    for a in arr:
        if a % 3 == 0:
            count += 1

    return count

def func_b(arr):#5의 배수 숫자
    count = 0
    for a in arr:
        if a % 5 == 0:
            count += 1
    return count

def func_c(three_count, five_count):
    if three_count > five_count:
        return 'three'
    elif five_count > three_count:
        return'five'
    else:
        return 'same'

def solution(arr):
    three_count = func_a(arr)
    five_count = func_b(arr)
    answer = func_c(three_count, five_count) 
    return answer

arr = [2, 3, 6, 9, 12, 15, 10, 220, 22, 25]
ret = solution(arr)
print(ret)

arr = [5, 5, 3]
ret = solution(arr)
print(ret)

arr = [30, 3, 5]
ret = solution(arr)
print(ret)