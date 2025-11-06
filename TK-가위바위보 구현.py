import random
from tkinter import *

window = Tk()
Label(window, text="선택하세요", font=("Helvetica", "16")).pack()
frame = Frame(window)
rock_image = PhotoImage(file="d:\\rock.png")
paper_image = PhotoImage(file="d:\\paper.png")
scissors_image = PhotoImage(file="d:\\scissors.png")

def pass_s():
    decide("가위")
def pass_r():
    decide("바위")
def pass_p():
    decide("보")

rock = Button(frame, image=rock_image, command=pass_r)
rock.pack(side="left")
paper = Button(frame, image=paper_image, command=pass_p)
paper.pack(side="left")
scissors = Button(frame, image=scissors_image, command=pass_s)
scissors.pack(side="left")

frame.pack()
Label(window, text="컴퓨터는 다음을 선택하였습니다.", font=("Helvetica", "16")).pack()

computer_image = Label(window, image=rock_image)
computer_image.pack()
output = Label(window, text="", font=("Helvetica", "16"))
output.pack()
def decide(human):
    computer = random.choice(["가위", "바위", "보"])
    if   computer == "바위":
        computer_image["image"] = rock_image
    elif   computer == "보":
        computer_image["image"] = paper_image
    else:
        computer_image["image"] = scissors_image

    if   (computer == "바위" and human == "보") or (computer == "보" and human == "가위")\
            or (computer == "가위" and human == "바위"):
        result = "인간 승리!"
    elif   computer == human:
        result = "비겼습니다."
    else:
        result = "컴퓨터 승리!"
    output.config(text="인간: " + human + "   컴퓨터:" + computer + "    " + result)


window.mainloop()

# 학습용 참고 (Label, frame, pack, grid, place ..)
# Label(부모창, 옵션들...) = 텍스트나 이미지를 보여주는 Tkinter 위젯
# 예시) Label(window, text="안녕하세요!", font=("Arial", 14), fg="blue").pack()

# Frame : 여러 개의 버튼이나 위젯을 한 덩어리로 묶기 위한 공간(틀)
# Tkinter에서 레이아웃을 깔끔하게 만들 때 자주 사용합니다.

# pack : 위젯을 창에 배치하는 메서드

# output.config : 표시 이미지 변경

#.pack() — 위아래, 왼쪽오른쪽으로 자동 정렬
#.grid() — 행/열 좌표에 맞춰 배치
#.place() — 좌표(x, y)로 직접 배치