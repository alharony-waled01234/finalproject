
from tkinter import *
from tkinter import messagebox
def dmain1():
    root=Tk()
    root.title('Dashboard')
    root.geometry("925x500+300+200")
    root.config(bg="#ECF9FF")
    root.resizable(False,False)

    label_doc=Label(root,text="مرحبا دكتوراسامه شفيق",fg="#331c48",bg="#ECF9FF",font=('Microsoft YaHei UI Light ',30))
    label_doc.place(x=150,y=100)
    label_doc.pack()


    #frame for subjects
    fram_one=Frame(root,width=250,height=230,bg="#0081C9").place(x=30,y=130)
    fram_two=Frame(root,width=250,height=230,bg="#0081C9").place(x=320,y=130)
    fram_three=Frame(root,width=250,height=230,bg="#0081C9").place(x=620,y=130)

    #frames for subjects
    Label(fram_one,text="Data Structure",bg="#0081C9",fg='white',font=('Microsoft YaHei UI Light ',15)).place(x=80,y=140)
    Label(fram_two,text="Data Base",bg="#0081C9",fg='white',font=('Microsoft YaHei UI Light ',15)).place(x=390,y=140)
    Label(fram_three,text="Structure Programming",bg="#0081C9",fg='white',font=('Microsoft YaHei UI Light ',15)).place(x=635,y=140)

    #frame one
    Label(fram_one,text="قسم حاسبات",bg="#0081C9",fg='white',font=('Microsoft YaHei UI Light ',15)).place(x=110,y=190)
    Label(fram_one,text="شعبه علوم حاسب",bg="#0081C9",fg='white',font=('Microsoft YaHei UI Light ',15)).place(x=90,y=240)

    #frame two
    Label(fram_two,text="قسم حاسبات",bg="#0081C9",fg='white',font=('Microsoft YaHei UI Light ',15)).place(x=400,y=190)
    Label(fram_two,text="شعبه علوم حاسب",bg="#0081C9",fg='white',font=('Microsoft YaHei UI Light ',15)).place(x=380,y=240)

    #frame three
    Label(fram_three,text="قسم حاسبات",bg="#0081C9",fg='white',font=('Microsoft YaHei UI Light ',15)).place(x=700,y=190)
    Label(fram_three,text="شعبه علوم حاسب",bg="#0081C9",fg='white',font=('Microsoft YaHei UI Light ',15)).place(x=680,y=240)


    Button(fram_one,width=10,pady=7,text="الدخول",bg="white",fg='black',border=0).place(x=110,y=310)
    Button(fram_two,width=10,pady=7,text="الدخول",bg="white",fg='black',border=0).place(x=405,y=310)
    Button(fram_three,width=10,pady=7,text="الدخول",bg="white",fg='black',border=0).place(x=710,y=310)
    root.mainloop()