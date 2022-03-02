from tkinter import *
from tkinter import messagebox

key = 0

def 키눌림(e):
    global key
    key = e.keysym
    
def 키떼짐(e):
    global key
    key = ""
   
mx = 1
my = 1

def 새로고침():
    global mx, my, x, y
    if key == 'Up' and maze[my-1][mx] != 1:
        my = my - 1
        #canvas.move(player, 0, -80)
    elif key == 'Down' and maze[my+1][mx] != 1:
        my = my + 1
        #canvas.move(player, 0, 80)
    elif key == 'Left' and maze[my][mx-1] != 1:
        mx = mx - 1
        #canvas.move(player, -80, 0)
    elif key == 'Right' and maze[my][mx+1] != 1:
        mx = mx + 1
        #canvas.move(player, 80, 0)
    elif key == 'space':
        mx = 1
        my = 1
        
    canvas.coords("CAT", mx*80 + 40, my*80 +40)  
    
    if maze[my][mx] == 2:
        messagebox.showinfo('미션 성공', '목적지에 도착했습니다')
    else:
        win.after(100, 새로고침)

win = Tk()
win.title("미로 찾기")
win.geometry("800x560")

canvas = Canvas(width=800, height=560, bg="white")
canvas.pack()

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 1],
    [1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 2, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

for y in range(7):
    for x in range(10):
        if maze[y][x] == 1:
            canvas.create_rectangle(x*80, y*80, (x*80)+80, (y*80)+80, fill='gray')
        elif maze[y][x] == 2:
            canvas.create_rectangle(x*80, y*80, (x*80)+80, (y*80)+80, fill='lightgreen')


img = PhotoImage(file='작은고양이.png')
player = canvas.create_image(mx * 80 + 40, my * 80 + 40, image=img, tag = "CAT")

win.bind("<KeyPress>", 키눌림)
win.bind("<KeyRelease>", 키떼짐)

새로고침()

win.mainloop()
