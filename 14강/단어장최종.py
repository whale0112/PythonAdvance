from tkinter import *
import random
import time

BG_COLOR = '#21325E'
BUTTON_COLOR = '#F0F0F0'
CORRECT_COLOR = '#F1D00A'

문제들 = []
#file = open('quiz.txt', 'r')
with open('quiz.txt', 'r') as file:
    for line in file.readlines():
        line = line.replace('\n', '')
        data = line.split('@')
        문제들.append(data)
#file.close 
print(문제들)

def 맨위로(frame):
    frame.tkraise()

정답 = 0

def 문제출력():
    global 정답
    문제후보 = random.sample(문제들, 4)
    정답 = random.randint(0, 3)
    현재질문 = 문제후보[정답][0]

    문제라벨.config(text=현재질문)
    for i in range(4):
        버튼들[i].config(text=문제후보[i][1])
        버튼들[i].config(bg = BG_COLOR)

def 정답확인(index):
    index = int(index)
    if 정답 == index:
        버튼들[index].config(bg = CORRECT_COLOR)
        time.sleep(0.5)
        문제출력()
    else:
        버튼들[index].config(bg = 'red')

def 단어출력():
    문제 = random.choice(문제들)
    단어라벨.config(text=문제[0])
    뜻라벨.config(text=문제[1])

win = Tk()
win.title('영어 단어장')

#메인메뉴 화면
메뉴프레임 = Frame(win)
메뉴프레임.grid(row=0, column=0, sticky='nsew')

타이틀라벨 = Label(메뉴프레임, width=20, height=2, text='단어장', font=('맑은고딕', 25, 'bold'), bg=BG_COLOR, fg='white')
타이틀라벨.pack()
문제풀기버튼 = Button(메뉴프레임, text='문제 풀기', width=15, height=2, font=('맑은고딕', 13, 'bold'), bg=CORRECT_COLOR, command=lambda : 맨위로(퀴즈프레임))
문제풀기버튼.pack(pady=30)
단어보기버튼 = Button(메뉴프레임, text='단어 보기', width=15, height=2, font=('맑은고딕', 13, 'bold'), bg=CORRECT_COLOR, command=lambda : 맨위로(단어프레임))
단어보기버튼.pack(pady=30)

#퀴즈화면
퀴즈프레임 = Frame(win)
퀴즈프레임.grid(row=0, column=0, sticky='nsew')

문제라벨 = Label(퀴즈프레임, width=20, height=2, text='테스트', font=('맑은고딕', 25, 'bold'), bg=BG_COLOR, fg='white')
문제라벨.pack()

#단어화면
단어프레임 = Frame(win)
단어프레임.grid(row=0, column=0, sticky='nsew')

단어라벨 = Label(단어프레임, width=20, height=2, text='테스트', font=('맑은고딕', 25, 'bold'), bg=BG_COLOR, fg='white')
단어라벨.pack()

뜻라벨 = Label(단어프레임, width=20, height=2, text='테스트', font=('맑은고딕', 25, 'bold'), bg=BG_COLOR, fg='white')
뜻라벨.pack()

다음버튼 = Button(단어프레임, text='다음단어', width=15, height=2, font=('맑은고딕', 13, 'bold'), bg=CORRECT_COLOR, command=단어출력)
다음버튼.pack(pady=30)

버튼들 = []

for number in range(4):
    버튼 = Button(퀴즈프레임, text='{}번'.format(number + 1), width=35, height=2, font=('맑은고딕', 13, 'bold'), 
                    bg=BG_COLOR, fg=BUTTON_COLOR, command=lambda index = number : 정답확인(index))
    버튼.pack()
    버튼들.append(버튼)

다음버튼 = Button(퀴즈프레임, text='다음문제', width=15, height=2, font=('맑은고딕', 13, 'bold'), bg=CORRECT_COLOR, command=문제출력)
다음버튼.pack(pady=30)

메인화면버튼 = Button(퀴즈프레임, text='메인화면', width=15, height=2, font=('맑은고딕', 13, 'bold'), bg=CORRECT_COLOR, command=lambda : 맨위로(메뉴프레임))
메인화면버튼.pack()

맨위로(메뉴프레임)
win.mainloop()
