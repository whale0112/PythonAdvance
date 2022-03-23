from tkinter import *

num = 0
def change():
    global num
    canvas.delete("CAT")
    canvas.create_image(400, 300, image=photo[num], tag="CAT")
    num = num+1
    if num >= 4:
        num = 0
    win.after(1000, change)

win = Tk()
win.title('디지털액자')

canvas = Canvas(width=800, height=600)
canvas.pack()
photo = [
    PhotoImage(file='cat00.png'),
    PhotoImage(file='cat01.png'),
    PhotoImage(file='cat02.png'),
    PhotoImage(file='cat03.png')
]

change()

win.mainloop()
