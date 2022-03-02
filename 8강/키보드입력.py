from tkinter import *

win = Tk()
win.title("이벤트 받기")
win.geometry("600x600")

key = 0

def key_down(e):
    global key
    key = e.keycode
    print("KEY : {}".format(key))

win.bind("<KeyPress>", key_down)

win.mainloop()
