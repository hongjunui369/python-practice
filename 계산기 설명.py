#버튼 테두리 효과 : relief, flat, raised, groove, ridge, sunken
#entry = Entry(부모창, 옵션들)

# 텍스트 가져오기
#text = entry.get()          # 입력된 전체 텍스트 반환
# 텍스트 설정하기
#entry.delete(0, END)        # 0번 위치부터 끝까지 삭제
#entry.insert(END, "텍스트")  # 끝에 텍스트 추가
#entry.insert(0, "텍스트")    # 처음에 텍스트 추가
# 기타 기능
#entry.config(state='disabled')  # 입력 비활성화
#entry.config(state='normal')    # 입력 활성화
#entry.focus()                   # 입력창에 포커스 주기

from tkinter import *

def click(key):
#click 함수 정의 시작, 버튼 클릭 시 호출됨
    if key == '=':		# “=” 버튼이면 수식을 계산하여 결과를 표시한다.
        try:
            result = eval(entry.get())
            #entry에 입력된 문자열을 Python 코드로 실행하여 계산
            entry.delete(0, END)
            entry.insert(END, str(result))
        except:
            entry.insert(END, "오류!")
    elif key == 'C':
        entry.delete(0, END)
    else:
        entry.insert(END, key)

window = Tk()
window.title("간단한 계산기")
buttons = [
'7',  '8',  '9',  '+',  'C',
'4',  '5',  '6',  '-',  '  ',
'1',  '2',  '3',  '*',  '  ',
'0',  '.',  '=',  '/',  '   ' ]

# 반복문으로 버튼을 생성한다.
i=0
for b in buttons:
    cmd = lambda x=b: click(x)
    b = Button(window,text=b,width=5,relief='ridge',command=cmd)
    b.grid(row=i//5+1,column=i%5)
    i += 1

# 엔트리 위젯은 맨 윗줄의 5개의 셀에 걸쳐서 배치된다.
entry = Entry(window, width=33, bg="yellow")
entry.grid(row=0, column=0, columnspan=5)

window.mainloop()
