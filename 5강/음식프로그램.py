from tkinter import *
win = Tk()
win.geometry('200x350')
win.title("내가 좋아하는 음식 리스트")

음식들 = ["돈까스", "초밥", "마라탕"]

lb = Listbox(win)
for 음식 in 음식들:
    lb.insert(END, 음식)
lb.pack()

entry = Entry(win, bg='light green')
entry.pack()

def 추가():
    음식 = entry.get()
    lb.insert(END, 음식)

btn = Button(win, text = '추가', command = 추가)
btn.pack()

def 삭제():
    lb.delete(lb.curselection())

btn2 = Button(win, text = "삭제", command = 삭제)
btn2.pack()

def 모두삭제():
    lb.delete(0, END)

btn3 = Button(win, text = "모두삭제", command = 모두삭제)
btn3.pack()

def 출력():
    print(lb.get(0, END))

btn4 = Button(win, text = '출력', command = 출력)
btn4.pack()

def 저장():
    음식들 = lb.get(0, END)
    print(음식들)

btn5 = Button(win, text = '저장', command = 저장)
btn5.pack()

win.mainloop()
