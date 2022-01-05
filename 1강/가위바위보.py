import random
sel = ['가위', '바위', '보']
resultDic = {0:'승리했습니다.', 1:'패배했습니다.', 2:'비겼습니다.'}
def checkwin(user, com):
    result = 0
    if user == '가위':
        if com == '가위':
            result = 2
        elif com == '바위':
            result = 1
        else:
            result = 0
    elif user == '바위':
        if com == '가위':
            result = 0
        elif com == '바위':
            result = 2
        else:
            result = 1
    else:
        if com == '가위':
            result = 1
        elif com == '바위':
            result = 0
        else:
            result = 2
    return resultDic[result]
print('-'*50)
user = input("가위, 바위, 보 : ")
print('-'*50)
com = sel[random.randint(0, 2)]
print('사용자 ( {} vs {} ) 컴퓨터'.format(user, com))
print(checkwin(user, com))
