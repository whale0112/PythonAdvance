from tkinter import *
import random

FRAME_RATE = 20
score = -1
NOW_PLAYING = True
SHOW_GAME_OVER = False

win = Tk()
win.resizable(False, False)
win.title('플래피버드')
win.geometry('550x700')

w = Canvas(win, width=550, height=700, background='#4EC0CA')
w.pack()

bird_y = 200
pipe_x = 350
pipe_hole = 100

bird_img = PhotoImage(file='bird.gif')
bird = w.create_image(100, bird_y, image=bird_img)

pipe_up = w.create_rectangle(pipe_x, 0, pipe_x + 100, pipe_hole, fill='#74BF2E', outline='#74BF2E')
pipe_down = w.create_rectangle(pipe_x, pipe_hole + 200, pipe_x + 100, 700, fill='#74BF2E', outline='#74BF2E')

score_w = w.create_text(15, 45, text='0', fill='white', font='Impact 60', anchor=W)

up_count = 0

end_rect = None
end_score = None

def 새점프(e = None):
    global bird_y, up_count

    if NOW_PLAYING == True:
        bird_y -= 20
        if bird_y <= 0:
            bird_y = 0
        w.coords(bird, 100, bird_y)
        if up_count > 0:
            up_count -= 1
            win.after(FRAME_RATE, 새점프)
        else:
            up_count = 5
    elif SHOW_GAME_OVER == True:
    #else:
        다시시작()


def 새중력():
    global bird_y

    bird_y += 8
    if bird_y >= 700:
        bird_y = 700
    w.coords(bird, 100, bird_y)
    if NOW_PLAYING == True:
         win.after(FRAME_RATE, 새중력)

def 파이프구멍변경():
    global pipe_hole, score
    pipe_hole = random.randint(50, 500)
    score += 1
    w.itemconfig(score_w, text=str(score))

def 파이프이동():
    global pipe_x
    pipe_x -=5
    w.coords(pipe_up, pipe_x, 0, pipe_x+100, pipe_hole)
    w.coords(pipe_down, pipe_x, pipe_hole+200, pipe_x + 100, 700)

    if pipe_x < -100:
        pipe_x = 550
        파이프구멍변경()

    if NOW_PLAYING == True:
        win.after(FRAME_RATE, 파이프이동)

def 게임오버화면():
    global end_rect, end_score
    end_rect = w.create_rectangle(0, 0, 550, 700, fill='#4EC0CA')
    end_score = w.create_text(15, 200, text='Your score: ' + str(score), fill='white', font='Impact 60', anchor=W)
    win.after(FRAME_RATE * 50, 게임오버데이터변경)

def 게임오버데이터변경():
    global SHOW_GAME_OVER
    SHOW_GAME_OVER = True

def 탐지():
    global NOW_PLAYING
    if (pipe_x < 150 and pipe_x + 100 >= 55) and (bird_y < pipe_hole + 50 or bird_y > pipe_hole + 200):
        NOW_PLAYING = False
        게임오버화면()

    if NOW_PLAYING == True:
        win.after(FRAME_RATE, 탐지)

def 다시시작():
    global NOW_PLAYING, SHOW_GAME_OVER
    global pipe_x, bird_y, score

    NOW_PLAYING = True
    SHOW_GAME_OVER = False
    pipe_x = 550
    bird_y = 200
    score = -1

    w.delete(end_rect)
    w.delete(end_score)

    새중력()
    파이프구멍변경()
    파이프이동()
    탐지()

win.after(FRAME_RATE, 새중력)
파이프구멍변경()
파이프이동()
탐지()

win.bind("<space>", 새점프)

win.mainloop()
