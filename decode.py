from email.mime import message
from pydoc import text
from tkinter import  *
from tkinter import font
from tkinter.messagebox import showerror, showwarning
from turtle import width
import encode_decode_fuction

window = Tk()
window.geometry("600x300+0+0")
window.title("app build by Thanh")
window.iconbitmap("icon.ico")
window.resizable(False, False)

def bt_click():
    text = ety.get()
    key = ety1.get()
    if key == "":
        showwarning("warning", "key is emty")
    if text == "":
        showwarning("warning", "text is emty")

    else:
        try:
            key = int(key)
            if key >= 1000 or key <= 0:
                showwarning("warning", "this key is 0 <= key <= 1000")
            else :
                en_text = encode_decode_fuction.decode(text, key=key)
                txt.delete("1.0", END)
                txt.insert("1.0", en_text)
        except:
            showerror("error", "there was wrong (key not int)")

def qut():
    window.destroy()


lbl = Label(window, text = "DECODE", bg = "green", font = "arial 20 bold", height=1)
lbl.pack()

lbl1 = Label(window, text="Text : ", font="sans 15 bold")
lbl1.place(x=30, y=45)

ety = Entry(window, font="sans 15", width=25)
ety.place(x=90, y=47.5)

lbl1 = Label(window, text="Space text : ", font="sans 15 bold")
lbl1.place(x=30, y=85)

ety1 = Entry(window, font="sans 15", width=13)
ety1.place(x=157, y=85.5)


btn = Button(window, text="decode", font="arial 13 ", bg="gray", fg="yellow", command=bt_click)
btn.place(x=320, y=85)

txt = Text(window, width=40, height=5, font="sans 15 bold", fg="white", bg="black")
txt.place(x=40, y=125)

# btn1 = Button(window, width=10, height=1, text="Quit", font="sans 10 bold", fg="red", activebackground="black", activeforeground="white", border=0.5, command=qut)
# btn1.place(x=0, y=270)

window.mainloop()
