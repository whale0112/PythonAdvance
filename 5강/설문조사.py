from tkinter import *

win = Tk()
win.geometry("350x400")
win.title('좋아하는 동물 선택')

라디오버튼그룹 = IntVar()

동물들 = {1:'고양이', 2:'강아지', 3:'오리', 4:'햄스터', 5:'호랑이'}

def 선택():
    print(동물들[라디오버튼그룹.get()])

label1 = Label(win, text='[1번문제] 당신이 좋아하는 동물은?')
label1.pack()
rb1 = Radiobutton(win, text = "1. 고양이", variable=라디오버튼그룹, value = 1, command=선택)
rb1.pack()
rb1 = Radiobutton(win, text = "2. 강아지", variable=라디오버튼그룹, value = 2, command=선택)
rb1.pack()
rb1 = Radiobutton(win, text = "3. 오리", variable=라디오버튼그룹, value = 3, command=선택)
rb1.pack()
rb1 = Radiobutton(win, text = "4. 햄스터", variable=라디오버튼그룹, value = 4, command=선택)
rb1.pack()
rb1 = Radiobutton(win, text = "5. 호랑이", variable=라디오버튼그룹, value = 5, command=선택)
rb1.pack()

win.mainloop()
