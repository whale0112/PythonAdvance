from tkinter import *
from tkinter import messagebox 

score = 50
question_count = 5
question_score = score//question_count

def submit():
    global score
    for variable in r_variable:
        score = score + (variable.get() * question_score)

    messagebox.showinfo("결과", "당신의 점수는 {}점 입니다.".format(score)) 
    score = 50

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
r_variable = [IntVar(), IntVar(), IntVar(), IntVar(), IntVar()]

# 문제1
question1 = Label(win, text = "친구가 시험을 잘 못봐서 슬퍼할때\n'나 시험을 잘 못본것 같아'", bg="#ddd") 
question1.place(x=50, y=100) 
rb11 = Radiobutton(win, text = "1. 다음에는 잘 될거야!", bg="#ddd", variable=r_variable[0], value=1) 
rb11.place(x=50, y=140) 
rb12 = Radiobutton(win, text = "2. 무슨 시험이었어? 몇 점 맞아서 그래?", bg="#ddd", variable=r_variable[0], value=-1) 
rb12.place(x=50, y=160) 

# 문제2
question2 = Label(win, text = "친구가 배탈이 났을때\n'나 배탈 난 것 같아'", bg="#ddd") 
question2.place(x=50, y=200) 
rb21 = Radiobutton(win, text = "1. 괜찮아? 많이 아파?", bg="#ddd", variable=r_variable[1], value=1) 
rb21.place(x=50, y=240) 
rb22 = Radiobutton(win, text = "2. 괜찮아? 뭐 먹었는데?", bg="#ddd", variable=r_variable[1], value=-1) 
rb22.place(x=50, y=260) 

# 문제3
question3 = Label(win, text = "친구가 아끼는 물건을 잃어버렸을때\n'나 물건이 없어졌어'", bg="#ddd") 
question3.place(x=50, y=300) 
rb31 = Radiobutton(win, text = "1. 너가 너무 아끼는건데 어떡해ㅠ", bg="#ddd", variable=r_variable[2], value=1) 
rb31.place(x=50, y=340) 
rb32 = Radiobutton(win, text = "2. 그 물건을 마지막으로 본데가 어디야?", bg="#ddd", variable=r_variable[2], value=-1) 
rb32.place(x=50, y=360) 

# 문제4
question4 = Label(win, text = "친구와의 약속시간에 늦었을때\n내가 할 말은?", bg="#ddd") 
question4.place(x=50, y=400) 
rb41 = Radiobutton(win, text = "1. 미안해ㅠㅠ 밖에서 기다리느라 많이 힘들었지.", bg="#ddd", variable=r_variable[3], value=1) 
rb41.place(x=50, y=440) 
rb42 = Radiobutton(win, text = "2. 미안해ㅠㅠ 집에서 엄마랑 얘기할게 있어서 조금 늦게 출발했어.", bg="#ddd", variable=r_variable[3], value=-1) 
rb42.place(x=50, y=460) 

# 문제5
question5 = Label(win, text = "친구와 미술 숙제에 대해서 얘기할때\n'너는 대충한것 같은데 왜이렇게 결과물이 좋아?'", bg="#ddd") 
question5.place(x=50, y=500) 
rb51 = Radiobutton(win, text = "1. 엄청 열심히 했는데 왜그래ㅠㅠ", bg="#ddd", variable=r_variable[4], value=1) 
rb51.place(x=50, y=540) 
rb52 = Radiobutton(win, text = "2. 나 재능있나봐ㅋㅋ 고마워!", bg="#ddd", variable=r_variable[4], value=-1) 
rb52.place(x=50, y=560) 

button = Button(text="진단하기", font=("Times New Roman", 32), command=submit)
button.place(x=400, y=600) 

win.mainloop()
