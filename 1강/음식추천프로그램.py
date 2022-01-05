import random
menus = ['치킨', '햄버거', '초밥', '마라탕', '스파게티', '돈까스', '김밥']
print("추천 가능한 음식")
print("="*50)
for menu in menus:
    print(menu)
print("="*50)
pick = random.choice(menus)
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
    pick = random.choice(menus)
    print(pick)
