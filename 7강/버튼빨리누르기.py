from tkinter import *
from tkinter import messagebox

time = 10
count = 0

def play():
    global time

    시작버튼.place(x=-1000, y=-1000)
    누르기버튼.place(x=60, y=80)

    if time > 0:
        time = time - 1
        시간.config(text='남은 시간 {}초'.format(time))
        win.after(1000, play)
    else:
        string = '{}점 입니다\n'.format(count)
        if count <= 20:
            string = string + "아직 갈길이 머네요."
        elif 20 < count <= 50:
            string = string + "꽤 하시는군요."
        else:
            string = string + "와우~대단하네요!"

        messagebox.showinfo("결과", string)

        누르기버튼.place(x=-1000, y=-1000)
        다시시작버튼.place(x=60, y=80)

def score():
    global count
    count = count + 1
    점수.config(text=count)
    
def retry():
    global time
    global count
    time = 10
    count = 0
    시간.config(text='남은 시간 {}초'.format(time))
    점수.config(text=count)
    다시시작버튼.place(x=-1000, y=-1000)
    시작버튼.place(x=60, y=80)
    
win = Tk()
win.title('버튼누르기')
win.geometry('200x200+500+100')

타이틀 = Label(win, text='버튼 빨리 누르기')
타이틀.pack()
시간 = Label(win, text='남은 시간 {}초'.format(time))
시간.pack()
점수 = Label(win, text=count)
점수.pack()

시작버튼 = Button(win, text="시작", width=10, height=2, command=play)
시작버튼.place(x=60, y=80)
누르기버튼 = Button(win, text = '누르기', width=10, height=2, command=score)
다시시작버튼 = Button(win, text = '다시시작', width=10, height=2, command=retry)

win.mainloop()
