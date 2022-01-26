from tkinter import *
from tkinter import messagebox as msg
win = Tk()

def click():
    id = entry1.get()
    password = entry2.get()
    msg.showinfo('로그인','아이디 : ' + id + "\n비밀번호 : " + password)

win.title("Login")
win.geometry("300x300")
label1 = Label(win, text = "아이디")
label1.grid(row=0, column = 0)
label2 = Label(win, text = "비밀번호")
label2.grid(row=1, column=0)
entry1 = Entry(win)
entry1.grid(row=0, column=1)
entry2 = Entry(win)
entry2.grid(row=1, column=1)
button = Button(win, text = "로그인", command = click)
button.grid(row=2, column=0)
win.mainloop()
