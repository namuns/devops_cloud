from tkinter import *
from tkinter import messagebox
# 버튼을 사용하여 알림 창 띄우기
def clickButton() :
    messagebox.showinfo('버튼 클릭', '버큰을 클릭했습니다.')

window = Tk()
window.title("버튼 이벤트 연습")
window.geometry("200x200")

button1 = Button(window, text="요기 눌러요", fg="black", bg="powder blue", command=clickButton)
button2 = Button(window, text="요기 눌러요", fg="black", bg="powder blue", command=clickButton)
button3 = Button(window, text="요기 눌러요", fg="black", bg="powder blue", command=clickButton)

button1.pack(side=TOP, fill=X, padx=10, pady=10)
button2.pack(side=TOP, fill=X, padx=10, pady=10)
button3.pack(side=TOP, fill=X, padx=10, pady=10)

window.mainloop()
