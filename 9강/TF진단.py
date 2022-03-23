from tkinter import *
from tkinter import messagebox as msb 

score = 50
question_count = 3
question_score = score//question_count

def submit():
    global score
    if r1.get() == 1:
        score = score + question_score
    else:
        score = score - question_score
    if r2.get() == 1:
        score = score + question_score
    else:
        score = score - question_score
    if r3.get() == 1:
        score = score + question_score
    else:
        score = score - question_score
    
    msb.showinfo("진단 결과", "당신의 점수는 {}점 입니다".format(score))
win = Tk() 
win.title("T와 F 진단") 
win.resizable(False, False) # 윈도우 창 크기 조절 불가

title = Label(win, text = "0에 가까울수록 T, 100에 가까울수록 F", fg="red") 
title.pack()

canvas = Canvas(win, width=600, height=700)
canvas.pack()
bgimg = PhotoImage(file='배경.png')
canvas.create_image(300, 350, image=bgimg)

# 데이터가 저장될 변수 생성
r1 = IntVar() 
r2 = IntVar() 
r3 = IntVar() 

# 문제1
question1 = Label(win, text = "친구가 시험을 잘 못봐서 슬퍼할때\n'나 시험을 잘 못본것 같아'", bg="#ddd") 
question1.place(x=50, y=100) 
rb11 = Radiobutton(win, text = "1. 다음에는 잘 될거야!", bg="#ddd", variable=r1, value=1) 
rb11.place(x=50, y=140) 
rb12 = Radiobutton(win, text = "2. 무슨 시험이었어? 몇 점 맞아서 그래?", bg="#ddd", variable=r1, value=2) 
rb12.place(x=50, y=160) 

# 문제2
question2 = Label(win, text = "친구가 배탈이 났을때\n'나 배탈 난 것 같아'", bg="#ddd") 
question2.place(x=50, y=200) 
rb21 = Radiobutton(win, text = "1. 괜찮아? 많이 아파?", bg="#ddd", variable=r2, value=1) 
rb21.place(x=50, y=240) 
rb22 = Radiobutton(win, text = "2. 괜찮아? 뭐 먹었는데?", bg="#ddd", variable=r2, value=2) 
rb22.place(x=50, y=260) 

# 문제3
question3 = Label(win, text = "친구가 아끼는 물건을 잃어버렸을때\n'나 물건이 없어졌어'", bg="#ddd") 
question3.place(x=50, y=300) 
rb31 = Radiobutton(win, text = "1. 너가 너무 아끼는건데 어떡해ㅠ", bg="#ddd", variable=r3, value=1) 
rb31.place(x=50, y=340) 
rb32 = Radiobutton(win, text = "2. 그 물건을 마지막으로 본데가 어디야?", bg="#ddd", variable=r3, value=2) 
rb32.place(x=50, y=360) 

button = Button(text="진단하기", font=("Times New Roman", 32), command=submit)
button.place(x=400, y=400) 

win.mainloop()
