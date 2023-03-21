from tkinter import *
from tkinter import messagebox

root=Tk()
root.title('Login')
root.geometry("925x500+300+200")
root.config(bg="#ECF9FF")
root.resizable(False,False)

img_logo = PhotoImage(file="E:\logo.png")
root.iconphoto(False,img_logo)
Label(root,image=img_logo, bg="white",background="#ECF9FF").place(x=50,y=120)
frame = Frame(root,width=350,height=370,bg="#ECF9FF")
frame.place(x=480,y=50)

heading = Label(frame,text="تعديل مادة",fg="black",bg="#ECF9FF",font=('Microsoft YaHei UI Light ',25,'bold'))
heading.place(x=100,y=-6)

def on_enter(e):
    section.delete(0,'end')
def on_leave(e):
    section_name = section.get()
    if section_name=='':
        section.insert(0, 'اسم الشعبة')

section = Entry(frame,width=35,fg='#181823',border=0,bg="#ECF9FF",font=('Microsoft YaHei UI Light ',15))
section.place(x=30,y=50)
section.insert(0,'اسم الشعبة')
section.bind('<FocusIn>',on_enter)
section.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=75)

def on_enter(e):
    material.delete(0,'end')
def on_leave(e):
    material_name = material.get()
    if material_name=='':
        material.insert(0, 'اسم المادة')

material = Entry(frame,width=35,fg='#181823',border=0,bg="#ECF9FF",font=('Microsoft YaHei UI Light ',15))
material.place(x=30,y=84)
material.insert(0,'اسم المادة')
material.bind('<FocusIn>',on_enter)
material.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=109)



def on_enter(e):
    tname.delete(0,'end')
def on_leave(e):
    teacher_name = tname.get()
    if teacher_name=='':
        tname.insert(0, 'اسم الدكتور الجديد')

tname = Entry(frame,width=35,fg='#181823',border=0,bg="#ECF9FF",font=('Microsoft YaHei UI Light ',15))
tname.place(x=30,y=118)
tname.insert(0,'اسم الدكتور الجديد')
tname.bind('<FocusIn>',on_enter)
tname.bind('<FocusOut>',on_leave)
Frame(frame,width=295,height=2,bg="black").place(x=25,y=143)


btn_login = Button(frame,width=39,pady=7,text="تعديل",bg="#57a1f8",fg='white',border=0)
btn_login.place(x=35,y=200)


root.mainloop()