def solution(attack, recovery, hp):
    a = attack - recovery
    b = hp // a
    if hp % a != 0:
        b += 1
    return b

attack = 30
recovery = 10
hp = 60
answer = solution(attack, recovery, hp)
print(answer)