from tkinter import *

win = Tk()
win.geometry("400x400")
win.title("배경색 바꾸기")

#버튼1 함수 
def click1(): 
    win.configure(background='red') 
#버튼2 함수 
def click2():
    win.configure(background='blue')
#버튼3 함수 
def click3():
    win.configure(background='yellow')
#버튼4 함수 
def click4():
    win.configure(background='purple')
#레이블 출력 
Label1 = Label(win, text = "버튼을 클릭해서 바탕화면의 색을 바꿔보세요!") 
Label1.pack() 

#버튼1 
Button1 = Button(win, text="빨간색", width=7, command=click1) 
Button1.pack() 
#버튼2 
Button2 = Button(win, text="파란색", width=7, command=click2)
Button2.pack()
#버튼3
Button3 = Button(win, text="노란색", width=7, command=click3)
Button3.pack()
#버튼4 
Button4 = Button(win, text="보라색", width=7, command=click4)
Button4.pack()
#메인 반복문 실행
win.mainloop()
