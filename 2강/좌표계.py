import turtle as t
def line(x1,y1,x2,y2):
    t.up()
    t.goto(x1,y1)
    t.down()
    t.goto(x2,y2)
    return
def write(x,y,text):
    t.up()
    t.goto(x,y)
    t.down()
    t.write(text)
    return
line(-500,0,500,0)
line(0,-500,0,500)
i = -500
while i <= 500:
    i = i + 100
    line(i, -5, i, 5)
    if i != 0:
        write(i-10, -20, i)
i = -500
while i <= 500:
    i = i + 100
    line(-5, i, 5, i)
    if i  != 0:
        write(7, i-5, i)
t.done()
