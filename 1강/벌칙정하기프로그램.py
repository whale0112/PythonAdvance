import random
벌칙들 = ['간식 사오기', '설거지', '인디언밥']
print("나올 수 있는 벌칙")
print('='*50)
for 벌칙 in 벌칙들:
    print(벌칙)
print('='*50)
pick = random.choice(벌칙들)
print(pick)
while True:
    user = input('다시 추천을 받으시겠습니까(예/아니오)? ')
    if user == '아니오':
        break
    elif user == '예':
        print('추천해드리겠습니다')
    else:
        print('잘못입력했습니다')
        continue
    pick = random.choice(벌칙들)
    print(pick)
    if pick == '인디언밥':
        print('인디언~밥!')
