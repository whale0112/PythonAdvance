from tkinter import *
win = Tk()
win.geometry("800x600")
win.title("Label 사용")
label1 = Label(win, text = "귀여운 강아지 사진", font=("굴림체", "20"))
label1.pack()
img = PhotoImage(file = "dog.png")
label2 = Label(win, image = img)
label2.pack()
win.mainloop()
