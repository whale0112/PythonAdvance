from tkinter import *
from tkinter import messagebox
import random

id = None

def move():
    변경x = random.randint(100, 500)
    변경y = random.randint(100, 500)
    파리버튼.place(x=변경x, y=변경y)
    delay = random.randint(300, 600)
    global id
    id = win.after(delay, move)
    # 1000ms -> 1초

def click():
    win.after_cancel(id)
    messagebox.showinfo("잡았다", "파리를 잡았습니다.\n축하해요")

def click2():
    move()

win = Tk()
win.title('파리잡기')
win.geometry('600x600')

img = PhotoImage(file='파리.png')
파리버튼 = Button(win, image=img, command=click)
파리버튼.place(x=300, y=300)

다시시작버튼 = Button(win, text = '다시시작', command = click2)
다시시작버튼.pack()

move()

win.mainloop()
