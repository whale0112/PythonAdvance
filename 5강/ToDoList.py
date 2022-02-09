from tkinter import *
win = Tk()
win.geometry('200x350')
win.title('To Do List')

할일들 = ['문제집 풀기', '영어책 읽기']

lb = Listbox(win)
for 할일 in 할일들:
    lb.insert(END, 할일)
lb.pack()

entry = Entry(win)
entry.pack()

def 추가():
    음식 = entry.get()
    lb.insert(END, 음식)

def 삭제():
    lb.delete(lb.curselection())

btn = Button(win, text = '할일 추가', command = 추가)
btn.pack()

btn2 = Button(win, text = '할일 삭제', command = 삭제)
btn2.pack()

win.mainloop()
