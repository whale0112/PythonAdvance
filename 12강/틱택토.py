from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("틱택토 게임")

#플레이어1라벨
p1_라벨 = Label(win, text="플레이어 1: ", height=1, width=8, font=('Serif', 20, 'bold'))
p1_이름 = Entry(win, bd=5)
p1_라벨.grid(row=0, column=0)
p1_이름.grid(row=0, column=1)

p2_라벨 = Label(win, text="플레이어 2: ", height=1, width=8, font=('Serif', 20, 'bold'))
p2_이름 = Entry(win, bd=5)
p2_라벨.grid(row=1, column=0)
p2_이름.grid(row=1, column=1)

def 재시작():
    global 순서, 클릭수
    버튼1['text'] = ' '
    버튼2['text'] = ' '
    버튼3['text'] = ' '
    버튼4['text'] = ' '
    버튼5['text'] = ' '
    버튼6['text'] = ' '
    버튼7['text'] = ' '
    버튼8['text'] = ' '
    버튼9['text'] = ' '
    순서 = 1
    클릭수 = 0

재시작버튼 = Button(win, text='재시작', height=1, width=8, command=재시작)
재시작버튼.grid(row=0, column=2)

#1또는 2
순서 = 1
#버튼이 다 눌렸는지 확인하는 변수
클릭수 = 0

def click(버튼):
    global 순서, 클릭수
    if 버튼['text'] == 'X' or 버튼['text'] == 'O':
        messagebox.showinfo('안내', '버튼이 이미 클릭되어 있습니다.')
        return

    if 순서 == 1:
        버튼.config(text='X')
        클릭수 += 1 # 클릭수 = 클릭수 + 1
        승리확인()
        순서 = 2

    elif 순서 == 2:
        버튼.config(text='O')
        클릭수 += 1
        승리확인()
        순서 = 1

def 승리확인():
    if ((버튼1['text'] != ' ' and 버튼1['text'] == 버튼2['text'] and 버튼2['text'] == 버튼3['text'])
    or (버튼4['text'] != ' ' and 버튼4['text'] == 버튼5['text'] and 버튼5['text'] == 버튼6['text'])
    or (버튼7['text'] != ' ' and 버튼7['text'] == 버튼8['text'] and 버튼8['text'] == 버튼9['text'])
    or (버튼1['text'] != ' ' and 버튼1['text'] == 버튼4['text'] and 버튼4['text'] == 버튼7['text'])
    or (버튼2['text'] != ' ' and 버튼2['text'] == 버튼5['text'] and 버튼5['text'] == 버튼8['text'])
    or (버튼3['text'] != ' ' and 버튼3['text'] == 버튼6['text'] and 버튼6['text'] == 버튼9['text'])
    or (버튼1['text'] != ' ' and 버튼1['text'] == 버튼5['text'] and 버튼5['text'] == 버튼9['text'])
    or (버튼3['text'] != ' ' and 버튼3['text'] == 버튼5['text'] and 버튼5['text'] == 버튼7['text'])):
        if 순서 == 1:
            messagebox.showinfo('결과', '{} 승리!!'.format(p1_이름.get()))
        else:
            messagebox.showinfo('결과', '{} 승리!!'.format(p2_이름.get()))
    elif 클릭수 == 9:
        messagebox.showinfo('결과', '무승부')


버튼1 = Button(win, text = ' ', command=lambda: click(버튼1), bg='gray', fg='black', height=4, width=8, font=('Serif', 20, 'bold'))
버튼1.grid(row=2, column=0)
버튼2 = Button(win, text = ' ', command=lambda: click(버튼2),bg='gray', fg='black', height=4, width=8, font=('Serif', 20, 'bold'))
버튼2.grid(row=2, column=1)
버튼3 = Button(win, text = ' ', command=lambda: click(버튼3),bg='gray', fg='black', height=4, width=8, font=('Serif', 20, 'bold'))
버튼3.grid(row=2, column=2)
버튼4 = Button(win, text = ' ', command=lambda: click(버튼4),bg='gray', fg='black', height=4, width=8, font=('Serif', 20, 'bold'))
버튼4.grid(row=3, column=0)
버튼5 = Button(win, text = ' ', command=lambda: click(버튼5),bg='gray', fg='black', height=4, width=8, font=('Serif', 20, 'bold'))
버튼5.grid(row=3, column=1)
버튼6 = Button(win, text = ' ', command=lambda: click(버튼6),bg='gray', fg='black', height=4, width=8, font=('Serif', 20, 'bold'))
버튼6.grid(row=3, column=2)
버튼7 = Button(win, text = ' ', command=lambda: click(버튼7),bg='gray', fg='black', height=4, width=8, font=('Serif', 20, 'bold'))
버튼7.grid(row=4, column=0)
버튼8 = Button(win, text = ' ', command=lambda: click(버튼8),bg='gray', fg='black', height=4, width=8, font=('Serif', 20, 'bold'))
버튼8.grid(row=4, column=1)
버튼9 = Button(win, text = ' ', command=lambda: click(버튼9),bg='gray', fg='black', height=4, width=8, font=('Serif', 20, 'bold'))
버튼9.grid(row=4, column=2)

win. mainloop()
