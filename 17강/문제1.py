def func_a(gloves):
    counter = [0] * 10
    for i in gloves:
        counter[i - 1] += 1

    return counter

def solution(left_gloves, right_gloves):
    left_counter = func_a(left_gloves)
    print(left_counter)
    right_counter = func_a(right_gloves)
    total = 0
    for i in range(0, 10, 1):
        a = min(left_counter[i], right_counter[i])
        total += a

    return total

left_gloves = [2, 1, 2, 2, 4]
right_gloves = [1, 2, 2, 4, 4, 7]
ret = solution(left_gloves, right_gloves)

print(ret)

left_gloves = [2, 1, 2, 2, 4, 2, 2, 2, 2]
right_gloves = [1, 2, 2, 4, 4, 7, 2, 2, 2, 2, 10]
ret = solution(left_gloves, right_gloves)

print(ret)
