from pydoc import text
from tkinter import  *

window = Tk()
window.geometry("600x300+0+200")
window.title("app build by Thanh")
window.iconbitmap("icon.ico")
window.resizable(False, False)

def de():
    import decode

def en():
    import encode

def rate():
    import rating

lbl = Label(window, text="ENCODE and DECODE", font="arial 15 bold", bg="black", fg="white")
lbl.pack()

btn = Button(window, text = "ENCODE", bg = "red", font = "arial 20 bold", width=10, height=3, command=en)
btn.place(x=50, y=50)

btn1 = Button(window, text = "DECODE", bg = "green", font = "arial 20 bold", width=10, height=3, command=de)
btn1.place(x=350, y=50)

btn2 = Button(window, text = "RATING", font = "arial 12 bold italic", width=6, height=1, bg="#84fffb", fg="#336179", border=0.7, activebackground="#84fffb", activeforeground="red", command=rate)
btn2.place(x=527, y=265)

Label(text="* App giải mã và mã hóa được viết bởi thanh", font="arial 10 bold italic").place(x=50, y=250)
Label(text="* Giúp thông tin an toàn hơn khi vận chuyển", font="arial 10 bold italic").place(x=50, y=270)


window.mainloop()
