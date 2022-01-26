from tkinter import *
from tkinter import messagebox as msg
window = Tk()
window.geometry('300x500')
window.title("메시지박스")
def msg1():
    str = msg.askquestion("메시지상자","파이썬을 종료할까요?")
    if str == 'yes':
        window.destroy()
    else:
        msg.showinfo("메시지상자","취소버튼을 \n 누르셨습니다")
def msg2():
    window.destroy()
    window.quit()
Bu1=Button(window, text='클릭', width = 10, command=msg1)
Bu1.pack(pady=5)
Bu2=Button(window, text='종료', width = 10, command=msg2)
Bu2.pack(pady=5)
window.mainloop()
