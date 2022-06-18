from tkinter import  *
from tkinter.messagebox import showerror, showinfo
import lst

window = Tk()
window.geometry("600x300+0+200")
window.title("app build by Thanh")
window.iconbitmap("icon.ico")
window.resizable(False, False)

def bt_click():
    ids = et.get()
    user = et1.get()
    pwd = et2.get()
    
    try :
        ids = int(ids)
        
        if user == lst.username[ids] and pwd == lst.password[ids]:
            showinfo("info", "login complete")
            window.destroy()
            import menu
        else:
            showerror("error", "login failed")
            showerror("error", "password or username is wrong")
    except Exception as bug:
        # print(bug)
        showerror("error", "id must be number (0 -> 9)")

Label(text="ID",font="arial 30 bold").pack()

et = Entry(font="sans 15")
et.pack()

Label(text="Username",font="arial 30 bold").pack()

et1 = Entry(font="sans 15")
et1.pack()

Label(text="Password",font="arial 30 bold").pack()

et2 = Entry(font="sans 15", show="*")
et2.pack()

Button(text="submit", font="sans 13", command=bt_click).pack()


window.mainloop()
