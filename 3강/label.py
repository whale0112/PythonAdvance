from tkinter import *
win = Tk()
win.geometry("400x400")
win.title("Label 시용")
label1 = Label(win, text = "파이썬 공부하기", font=("궁서체","24"), width=25, height=4, anchor=S, foreground="red", background="blue")
label1.pack()
label2 = Label(win, text = "Python", font=("맑은고딕","15"), width=25, height=3, anchor=CENTER, foreground="purple", background="pink")
label2.pack()
win.mainloop()
