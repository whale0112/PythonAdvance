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

win = Tk()
win.title('영어 단어장')

문제라벨 = Label(win, width=20, height=2, text='테스트', font=('맑은고딕', 25, 'bold'), bg=BG_COLOR, fg='white')
문제라벨.pack()

버튼들 = []

for number in range(4):
    버튼 = Button(win, text='{}번'.format(number + 1), width=35, height=2, font=('맑은고딕', 13, 'bold'), 
                    bg=BG_COLOR, fg=BUTTON_COLOR, command=lambda index = number : 정답확인(index))
    버튼.pack()
    버튼들.append(버튼)

다음버튼 = Button(win, text='다음문제', width=15, height=2, font=('맑은고딕', 13, 'bold'), bg=CORRECT_COLOR, command=문제출력)
다음버튼.pack(pady=30)

win.mainloop()
