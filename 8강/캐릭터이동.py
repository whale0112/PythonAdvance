from tkinter import *

key = 0

def 키눌림(e):
    global key
    key = e.keysym

def 키떼짐(e):
    global key
    key = ""
   
x = 300
y = 300
def 새로고침():
    global x, y
    if key == 'Up':
        y = y - 20
    elif key == 'Down':
        y = y + 20
    elif key == 'Left':
        x = x - 20
    elif key == 'Right':
        x = x + 20
    canvas.coords("CAT", x, y)    
    win.after(100, 새로고침)

win = Tk()
win.title("캐릭터 이동")
win.geometry("600x600")

canvas = Canvas(width=600, height=600, bg='lightgreen')
canvas.pack()
img = PhotoImage(file="작은고양이.png")
canvas.create_image(300, 300, image=img, tag="CAT")

win.bind("<KeyPress>", 키눌림)
win.bind("<KeyRelease>", 키떼짐)

새로고침()

win.mainloop()
