


def solution(floors):
    dist = 0
    for i in range(0, len(floors) - 1, 1):
        if floors[i] > floors[i + 1]:
            a = floors[i]
            b =  floors[i + 1]
        else:
            a = floors[i + 1]
            b = floors[i]
        dist = dist + a - b

    return dist

floors = [1, 2, 5, 4, 2]
ret = solution(floors)
print(ret)

floors = [1, 12, 5, 4, 7]
ret = solution(floors)
print(ret)