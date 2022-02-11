from tkinter import *
from tkinter import messagebox as m
import webbrowser

window = Tk()
window.geometry("600x300+0+200")
window.title("app build by Thanh")
window.iconbitmap("icon.ico")

def click():
    star = sc.get()
    if star == 1 :
        m.showinfo("info", "thank for rating I will develop this app for more beautiful")
    elif star in (2,3):
        m.showinfo("info", "thank for rating")
    else:
        m.showinfo("info", "thank !!!")
    
    yn = m.askquestion("ask", "ban co muon vao 1 wedsite hay khong")
    if yn == "yes":
        webbrowser.open("http://weavesilk.com/")
    else:
        m.showinfo("info", "thanks")
        window.destroy()

sc = Scale(window, from_=1, to=5, length=250)
sc.set(value=5)
sc.pack()

btn = Button(window, text="rate", width=3, height=1, fg="red", font="arial 20", command=click)
btn.pack()

Label(window, text="+Rating this app", font="sans 15 italic bold").place(x=0, y=0)

window.mainloop()