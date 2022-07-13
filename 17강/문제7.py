def solution(value, unit):
    if unit == "F":
        a = (value - 32) / 1.8
    else:
        a = (value * 1.8) + 32

    return a

value = 527
unit = "C"
answer = solution(value, unit)
print(int(answer))