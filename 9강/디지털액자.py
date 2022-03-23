from tkinter import *

num = 0
def change():
    global num
    canvas.delete("CAT")
    if num == 0:
        canvas.create_image(400, 300, image=photo1, tag="CAT")
    elif num == 1:
        canvas.create_image(400, 300, image=photo2, tag="CAT")
    elif num == 2:
        canvas.create_image(400, 300, image=photo3, tag="CAT")
    elif num == 3:
        canvas.create_image(400, 300, image=photo4, tag="CAT")
    num = num+1
    if num >= 4:
        num = 0
    win.after(1000, change)

win = Tk()
win.title('디지털액자')

canvas = Canvas(width=800, height=600)
canvas.pack()
photo1 = PhotoImage(file='cat00.png')
photo2 = PhotoImage(file='cat01.png')
photo3 = PhotoImage(file='cat02.png')
photo4 = PhotoImage(file='cat03.png')

change()
canvas.create_image(400,300, image=photo1, tag="CAT")

win.mainloop()
