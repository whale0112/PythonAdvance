from tkinter import *
from tkinter import messagebox

def check1():
    str = ''
    if checkVar1.get() == 1:
        str = str + "고양이"
    if checkVar2.get() == 1:
        str = str + "강아지"
    if checkVar3.get() == 1:
        str = str + "토끼"
    if checkVar4.get() == 1:
        str = str + "햄스터"
    if checkVar5.get() == 1:
        str = str + "오리"
    if str=='':
        show1.config(text = "다 싫어요")
    else:
        show1.config(text = str + "를 좋아합니다")
def end1():
    win.destroy()

def check2():
    str2 = ''
    if checkVar6.get() == 1:
        str2 = str2 + "국어"
    if checkVar7.get() == 1:
        str2 = str2 + "수학"
    if checkVar8.get() == 1:
        str2= str2 + "사회"
    if checkVar9.get() == 1:
        str2 = str2 + "과학"
    if checkVar10.get() == 1:
        str2= str2 + "체육"
    if str2=='':
        show2.config(text = "다 싫어요")
    else:
        show2.config(text = str2 + "를 좋아합니다")
def 저장():
    str = ''
    if checkVar1.get() == 1:
        str = str + "고양이"
    if checkVar2.get() == 1:
        str = str + "강아지"
    if checkVar3.get() == 1:
        str = str + "토끼"
    if checkVar4.get() == 1:
        str = str + "햄스터"
    if checkVar5.get() == 1:
        str = str + "오리"
    if str=='':
        str = "다 싫어요"
    else:
        str = str + "를 좋아합니다"
    str2 = ''
    if checkVar6.get() == 1:
        str2 = str2 + "국어"
    if checkVar7.get() == 1:
        str2 = str2 + "수학"
    if checkVar8.get() == 1:
        str2= str2 + "사회"
    if checkVar9.get() == 1:
        str2 = str2 + "과학"
    if checkVar10.get() == 1:
        str2= str2 + "체육"
    if str2=='':
        str2 = "다 싫어요"
    else:
        str2 = str2 + "를 좋아합니다"
    
    f = open("설문조사결과.txt", 'w')
    f.write(str)
    f.write(str2)
    f.close()

win = Tk()
win.title("설문조사")
win.geometry("500x600")

checkVar1 = IntVar()
checkVar2 = IntVar()
checkVar3 = IntVar()
checkVar4 = IntVar()
checkVar5 = IntVar()
checkVar6 = IntVar()
checkVar7 = IntVar()
checkVar8 = IntVar()
checkVar9 = IntVar()
checkVar10 = IntVar()


label1 = Label(win, text = "[1번 문제] 당신이 가장 좋아하는 동물을 모두 선택하세요")
label1.pack()

cb1 = Checkbutton(win, text = "1. 고양이", variable=checkVar1)
cb1.pack()
cb2 = Checkbutton(win, text = "2. 강아지", variable=checkVar2)
cb2.pack()
cb3 = Checkbutton(win, text = "3. 토끼", variable=checkVar3)
cb3.pack()
cb4 = Checkbutton(win, text = "4. 햄스터", variable=checkVar4)
cb4.pack()
cb5 = Checkbutton(win, text = "5. 오리", variable=checkVar5)
cb5.pack()

show1=Label(win, text = "여기에 출력됩니다")
show1.pack()

확인버튼 = Button(win, text = "확 인", width=10, command=check1)
확인버튼.pack()
종료버튼 = Button(win, text = "종 료", width=10, command=end1)
종료버튼.pack()

label1 = Label(win, text = "[2번 문제] 당신이 가장 좋아하는 과목을 모두 선택하세요")
label1.pack()

cb6 = Checkbutton(win, text = "1. 국어", variable=checkVar6)
cb6.pack()
cb7 = Checkbutton(win, text = "2. 수학", variable=checkVar7)
cb7.pack()
cb8 = Checkbutton(win, text = "3. 사회", variable=checkVar8)
cb8.pack()
cb9 = Checkbutton(win, text = "4. 과학", variable=checkVar9)
cb9.pack()
cb10 = Checkbutton(win, text = "5. 체육", variable=checkVar10)
cb10.pack()

show2=Label(win, text = "여기에 출력됩니다")
show2.pack()

확인버튼 = Button(win, text = "확 인", width=10, command=check2)
확인버튼.pack()
종료버튼 = Button(win, text = "종 료", width=10, command=end1)
종료버튼.pack()
저장버튼 = Button(win, text = "저 장", width=10, command=저장)
저장버튼.pack()

win.mainloop()
