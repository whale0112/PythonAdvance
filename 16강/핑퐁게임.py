from tkinter import *
from tkinter import messagebox

FRAME = 20

win = Tk()

win.title('핑퐁게임')
c = Canvas(win, width=500, height=500, bg='skyblue')
c.pack()

패들 = c.create_rectangle(0, 0, 100, 20, fill='black')
공 = c.create_oval(0, 0, 20, 20, fill='red')

패들x = 250
공x = 250
공y = 250
공변경x = 5
공변경y = 5
속도 = 1

점수 = 0
베스트점수 = 0

c.coords(패들, 패들x-50, 460, 패들x+50, 440)
c.coords(공, 공x-10, 공y-10, 공x+10, 공y+10)

오른쪽눌림 = False
왼쪽눌림 = False

게임중 = True

def move_패들():
    global 패들x
    if 오른쪽눌림 and 패들x < 451:
        패들x += 10
    if 왼쪽눌림 and 패들x > 49:
        패들x -= 10

    c.coords(패들, 패들x-50, 460, 패들x+50, 440)
    if 게임중:
        win.after(FRAME, move_패들)

def move_공():
    global 공x, 공y, 공변경x, 공변경y, 점수, 속도
    공x = 공x + 공변경x
    공y = 공y + 공변경y

    if 공x > 489:
        공변경x = -5 * 속도
    elif 공x < 11:
        공변경x = 5 * 속도
    if 공y > 489:
        공변경y = -5 * 속도
    elif 공y < 11:
        공변경y = 5 * 속도
    
    if 공x > 패들x-51 and 공x < 패들x + 51 and 공y > 439:
        공변경y = 공변경y - 공변경y * 2
        점수 = 점수 + 1
        if 점수 % 5 == 0:
            속도 += 0.2

    c.coords(공, 공x-10, 공y-10, 공x+10, 공y+10)
    if 게임중:
        win.after(FRAME, move_공)

def on_press(e):
    global 오른쪽눌림, 왼쪽눌림
    if e.keysym == "Left":
        왼쪽눌림 = True
    if e.keysym == 'Right':
        오른쪽눌림 = True
def on_release(e):
    global 오른쪽눌림, 왼쪽눌림
    if e.keysym == "Left":
        왼쪽눌림 = False
    if e.keysym == 'Right':
        오른쪽눌림 = False

def check_gameover():
    global 게임중, 베스트점수
    if 공y > 480:
        게임중 = False

    if 게임중:
        win.after(FRAME, check_gameover)
    else:
        if 점수 > 베스트점수:
            베스트점수 = 점수
        messagebox.showinfo('결과', '{}점 입니다\n베스트점수는 {}점 입니다'.format(점수, 베스트점수))

def 다시시작():
    global 패들x, 공x, 공y, 점수, 게임중
    패들x = 250
    공x = 250
    공y = 250
    점수 = 0
    게임중 = True
    move_패들()
    move_공()
    check_gameover()

win.bind('<KeyPress>', on_press)
win.bind('<KeyRelease>', on_release)

다시시작버튼 = Button(win, text='다시시작', command=다시시작)
다시시작버튼.pack()

move_패들()
move_공()
check_gameover()

win.mainloop()
