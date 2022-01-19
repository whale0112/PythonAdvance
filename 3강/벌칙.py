from tkinter import *
import random
win = Tk()
벌칙들 = ['간식 사오기', '설거지', '인디언밥']
def pick():
    label.config(text = random.choice(벌칙들))
button = Button(win, text = "벌칙", command = pick)
button.pack()
label = Label(win)
label.pack()
win.mainloop()
