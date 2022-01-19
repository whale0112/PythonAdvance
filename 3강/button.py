from tkinter import *
win = Tk()
win.geometry("400x400")
win.title("Button 사용")
def alert():
    print("버튼이 눌림")
btn = Button(win)
btn.config(width = 20, height = 20)
btn.config(text = "버튼")
btn.config(command = alert)
btn.pack()
win.mainloop()
