from tkinter import *

win = Tk()
win.title('분식집 주문 프로그램')
win.geometry('600x400')

틀1 = Frame(win, width='600', height='10')
틀1.pack()
틀2 = Frame(win, width='600', height='10')
틀2.pack()
틀3 = Frame(win, width='600', height='10')
#틀3.pack()
틀4 = Frame(win, width='600', height='10')
틀4.pack()

def 음식메뉴보이기():
    음식버튼.configure(bg='yellow')
    음료버튼.configure(bg='white')
    틀2.pack() #음식메뉴 보이기
    틀3.pack_forget() #음료메뉴 숨기기
    틀4.pack_forget()
    틀4.pack()
def 음료메뉴보이기():
    음식버튼.configure(bg='white')
    음료버튼.configure(bg='yellow')
    틀3.pack() #음식메뉴 보이기
    틀2.pack_forget() #음료메뉴 숨기기
    틀4.pack_forget()
    틀4.pack()

음식_주문내역 = {}
음료_주문내역 = {}
음식_가격 = {'김밥':3000, '떡볶이':4500, '튀김':4500, '라면':3500, '쫄면':7500}
음료_가격 = {'콜라':3000, '쿨피스':3500, '레몬에이드':4500, '아이스티':4000, '주스':3500}
주문금액 = 0

def 음식주문(음식):
    global 음식_주문내역, 주문금액

    if 음식 in 음식_주문내역:
        음식_주문내역[음식] = 음식_주문내역.get(음식) + 1
    else:
        음식_주문내역[음식] = 1

    주문금액 = 주문금액 + 음식_가격[음식]

    주문출력()
    가격출력()

def 주문출력():
    출력할문자열 = ''
    for 주문내역 in 음식_주문내역:
        출력할문자열 = 출력할문자열 + "{} x {}\n".format(주문내역, str(음식_주문내역.get(주문내역)))
    for 주문내역 in 음료_주문내역:
        출력할문자열 = 출력할문자열 + "{} x {}\n".format(주문내역, str(음료_주문내역.get(주문내역)))

    주문서.delete('1.0', END)
    주문서.insert('1.0', 출력할문자열)

def 음료주문(음료):
    global 음료_주문내역, 주문금액

    if 음료 in 음료_주문내역:
        음료_주문내역[음료] = 음료_주문내역.get(음료) + 1
    else:
        음료_주문내역[음료] = 1

    주문금액 = 주문금액 + 음료_가격[음료]
    
    주문출력()
    가격출력()

def 가격출력():
    주문금액라벨.config(text='{} 원'.format(주문금액))

def 초기화():
    global 음식_주문내역, 음료_주문내역, 주문금액
    음식_주문내역 = {}
    음료_주문내역 = {}
    주문금액 = 0
    주문출력()
    가격출력()

음식버튼 = Button(틀1, text='음식', bg='yellow', command=음식메뉴보이기)
음식버튼.grid(row=0, column=0)
음료버튼 = Button(틀1, text='음료', bg='white', command=음료메뉴보이기)
음료버튼.grid(row=0, column=1)
주문종료버튼 = Button(틀1, text='초기화', command=초기화)
주문종료버튼.grid(row=0, column=2)
주문금액라벨 = Label(틀1, text='0 원')
주문금액라벨.grid(row=0, column=3, padx=10, pady=10)

음식1 = Button(틀2, text='김밥\n3000원', width='10', padx=10, pady=10, command=lambda: 음식주문('김밥'))
음식1.grid(row=0, column=0, padx=10, pady=10)
음식2 = Button(틀2, text='떡볶이\n4500원', width='10', padx=10, pady=10, command=lambda: 음식주문('떡볶이'))
음식2.grid(row=0, column=1, padx=10, pady=10)
음식3 = Button(틀2, text='튀김\n4500원', width='10', padx=10, pady=10, command=lambda: 음식주문('튀김'))
음식3.grid(row=0, column=2, padx=10, pady=10)
음식4 = Button(틀2, text='라면\n3500원', width='10', padx=10, pady=10, command=lambda: 음식주문('라면'))
음식4.grid(row=0, column=3, padx=10, pady=10)
음식5 = Button(틀2, text='쫄면\n7500원', width='10', padx=10, pady=10, command=lambda: 음식주문('쫄면'))
음식5.grid(row=0, column=4, padx=10, pady=10)

음료1 = Button(틀3, text='콜라\n3000원', width='10', padx=10, pady=10, command=lambda: 음료주문('콜라'))
음료1.grid(row=0, column=0, padx=10, pady=10)
음료2 = Button(틀3, text='쿨피스\n3500원', width='10', padx=10, pady=10, command=lambda: 음료주문('쿨피스'))
음료2.grid(row=0, column=1, padx=10, pady=10)
음료3 = Button(틀3, text='레몬에이드\n4500원', width='10', padx=10, pady=10, command=lambda: 음료주문('레몬에이드'))
음료3.grid(row=0, column=2, padx=10, pady=10)
음료4 = Button(틀3, text='아이스티\n4000원', width='10', padx=10, pady=10, command=lambda: 음료주문('아이스티'))
음료4.grid(row=0, column=3, padx=10, pady=10)
음료5 = Button(틀3, text='주스\n3500원', width='10', padx=10, pady=10, command=lambda: 음료주문('주스'))
음료5.grid(row=0, column=4, padx=10, pady=10)

주문서 = Text(틀4, height='10')
주문서.pack()

win.mainloop()
