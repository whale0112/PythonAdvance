from tkinter import *
import random
from tkinter import messagebox

win = Tk()
win.title('컬러게임')
win.geometry('450x400')

색상들 = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Orange', 'Yellow', 'Purple']
한글변환 = {'Red':'빨강', 'Blue':'파랑', 'Green':'초록', 'Pink':'분홍', 'Black':'검정', 'Orange':'주황', 'Yellow':'노랑', 'Purple':'보라'}
점수 = 1
남은시간 = 30
#시간줄이는 함수 호출하는 id
id = 0
최고점수 = 0

def 시간줄이기():
    global 남은시간, id, 최고점수
    #남은시간 = 남은시간 - 1
    남은시간 -= 1
    시간라벨.config(text='남은시간: {}'.format(남은시간))
    if 남은시간 > 0:
        id = win.after(1000, 시간줄이기)
    elif 남은시간 == 0:
        if 최고점수 < 점수:
            최고점수 = 점수
        messagebox.showinfo('점수', '점수 : {}점\n최고점수 : {}점'.format(점수, 최고점수))

def 다음문제():
    global 점수
    색 = 색상들[1]
    if 입력창.get().lower() == 한글변환[색].lower():
        #점수 = 점수 + 1
        점수 += 1
    else:
        점수 -= 1
    입력창.delete(0, END)
    random.shuffle(색상들)
    텍스트 = 색상들[0]
    한글텍스트 = 한글변환[텍스트]
    문제라벨.config(fg=색상들[1], text=한글텍스트)
    점수라벨.config(text='점수: ' + str(점수))
    입력창.focus_set()

def 게임시작(event):
    if 남은시간 == 30:
        시간줄이기()

    if 남은시간 > 0:
        다음문제()

def 초기화():
    global 점수, 남은시간
    win.after_cancel(id)
    점수 = 1
    남은시간 = 30
    점수라벨.config(text='엔터를 누르면 시작합니다.')
    시간라벨.config(text='남은 시간 : 30')
        
설명라벨 = Label(win, text='화면에 나오는 글자의 색상을 입력하세요!\n빨강, 주황, 노랑, 초록, 파랑, 보라, 분홍, 검정이 있습니다')
설명라벨.pack()
점수라벨 = Label(win, text='엔터를 누르면 시작합니다.')
점수라벨.pack()
시간라벨 = Label(win, text='남은 시간 : 30')
시간라벨.pack()
문제라벨 = Label(win, font=('Serif', 100))
문제라벨.pack()

입력창 = Entry(win)
입력창.pack()
입력창.focus_set()

초기화버튼 = Button(win, text='초기화', width=20, command=초기화)
초기화버튼.pack()

win.bind('<Return>', 게임시작)

win.mainloop()
