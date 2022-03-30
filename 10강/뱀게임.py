from tkinter import *
from tkinter import messagebox
import math
import random

win = Tk()
윈도우크기 = [625,625]
#625x625
win.geometry(str(윈도우크기[0]) + "x" + str(윈도우크기[1]))
win.resizable(False, False)
win.title('뱀 게임')

#윈도우 크기와 동일한 캔버스 생성
게임캔버스 = Canvas(win, width=윈도우크기[0], height=윈도우크기[1])
게임캔버스.pack()

한칸크기 = 25
#game_sizes = [25x25]
game_sizes = [윈도우크기[0]/한칸크기, 윈도우크기[1]/한칸크기]

#플레이어 좌표 (화면 가운데 좌표)
#math.floor 내림해서 점수 반환
플레이어좌표 = [math.floor(game_sizes[0]/2), math.floor(game_sizes[1]/2)]
플레이어몸통 = []

플레이어방향 = [1, 0]

def 사과좌표생성():
    x = random.randint(0, game_sizes[0] - 1)
    y = random.randint(0, game_sizes[1] - 1)
    좌표 = [x, y]

    for 마디 in 플레이어몸통:
        if 마디[0] == x and 마디[1] == y:
            return 사과좌표생성()
    
    return 좌표

사과좌표 = 사과좌표생성()

def 네모그리기(좌표, 색):
    x0 = 좌표[0] * 한칸크기
    y0 = 좌표[1] * 한칸크기
    x1 = (좌표[0]+1) * 한칸크기
    y1 = (좌표[1]+1) * 한칸크기
    게임캔버스.create_rectangle(x0, y0, x1, y1, fill=색, outline='#222222', width=3)

def gameloop():
    global 게임캔버스
    global 플레이어좌표
    global 사과좌표
    global 플레이어몸통
    global 플레이어방향
    # 100ms, 0.1초
    win.after(100, gameloop)
    게임캔버스.delete('all')
    게임캔버스.create_rectangle(0, 0, 윈도우크기[0], 윈도우크기[1], fill="#222222", outline='#222222')

    플레이어몸통.append([플레이어좌표[0], 플레이어좌표[1]])
    # 플레이어 좌표 이동
    플레이어좌표[0] += 플레이어방향[0]
    플레이어좌표[1] += 플레이어방향[1]

    if 플레이어좌표[0] == game_sizes[0]:
        플레이어좌표[0] = 0
    elif 플레이어좌표[0] == -1:
        플레이어좌표[0] = game_sizes[0] - 1
    elif 플레이어좌표[1] == game_sizes[1]:
        플레이어좌표[1] = 0
    elif 플레이어좌표[1] == -1:
        플레이어좌표[1] = game_sizes[1] - 1

    for 마디 in 플레이어몸통:
        if 마디[0] == 플레이어좌표[0] and 마디[1] == 플레이어좌표[1]:
            플레이어좌표 = [math.floor(game_sizes[0]/2), math.floor(game_sizes[1]/2)]
            플레이어몸통 = []
            플레이어방향 = [1, 0] 
            사과좌표 = 사과좌표생성()

        네모그리기(마디, '#00ff00')

    number = random.randint(0, 10)
    if number == 1:
        네모그리기(사과좌표, 'blue')
    else:
        네모그리기(사과좌표, '#ff0000')   

    if 사과좌표[0] == 플레이어좌표[0] and 사과좌표[1] == 플레이어좌표[1]:
        사과좌표 = 사과좌표생성()
    else:
        플레이어몸통.pop(0)  

def 키눌림(e):
    global 플레이어방향
    if e.keysym == 'Left' and 플레이어방향[0] != 1:
        플레이어방향 = [-1, 0]  
    if e.keysym == 'Right' and 플레이어방향[0] != -1:
        플레이어방향 = [1, 0]
    if e.keysym == 'Up' and 플레이어방향[1] != 1:
        플레이어방향 = [0, -1]
    if e.keysym == 'Down' and 플레이어방향[1] != -1:
        플레이어방향 = [0, 1]

win.bind("<KeyPress>", 키눌림) 

gameloop()

win.mainloop()
