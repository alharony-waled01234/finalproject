from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Login')
root.geometry("925x500+300+200")
root.config(bg="#ECF9FF")
root.resizable(False, False)

img_logo = PhotoImage(file="E:\logo.png")
root.iconphoto(False, img_logo)
Label(root, image=img_logo, bg="white", background="#ECF9FF").place(x=50, y=120)
frame = Frame(root, width=350, height=370, bg="#ECF9FF")
frame.place(x=480, y=50)

heading = Label(frame, text="انشاء حساب جديد", fg="black", bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 25, 'bold'))
heading.place(x=100, y=-6)


def on_enter(e):
    user.delete(0, 'end')


def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'عنوان البريد الالكتروني')


user = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
user.place(x=30, y=50)
user.insert(0, 'عنوان البريد الالكتروني')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=75)


def on_enter(e):
    code.delete(0, 'end')


def on_leave(e):
    password = code.get()
    if password == '':
        code.insert(0, 'كلمه السر')


code = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
code.place(x=30, y=84)
code.insert(0, 'كلمه السر')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=109)


def on_enter(e):
    tname.delete(0, 'end')


def on_leave(e):
    teacher_name = tname.get()
    if teacher_name == '':
        tname.insert(0, 'اسم المستخدم')


tname = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
tname.place(x=30, y=118)
tname.insert(0, 'اسم المستخدم')
tname.bind('<FocusIn>', on_enter)
tname.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=143)


def on_enter(e):
    institute.delete(0, 'end')


def on_leave(e):
    institute_name = institute.get()
    if institute_name == '':
        institute.insert(0, 'اسم المعهد')


institute = Entry(frame, width=35, fg='#181823', border=0, bg="#ECF9FF", font=('Microsoft YaHei UI Light ', 15))
institute.place(x=30, y=152)
institute.insert(0, 'اسم المعهد')
institute.bind('<FocusIn>', on_enter)
institute.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

btn_login = Button(frame, width=39, pady=7, text="التسجيل", bg="#57a1f8", fg='white', border=0)
btn_login.place(x=35, y=340)

root.mainloop()