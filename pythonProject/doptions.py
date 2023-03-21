from tkinter import *
import cv2

class Doptions:
    root=Tk()
    root.title("Attendance System")

    root.geometry("925x500+300+200")
    root.config(bg="#ECF9FF")
    root.resizable(False,False)

    img_logo = PhotoImage(file="E:\logo.png")
    root.iconphoto(False,img_logo)
    Label(root,image=img_logo, bg="white",background="#ECF9FF").place(x=50,y=120)
    frame = Frame(root,width=350,height=370,bg="#ECF9FF")
    frame.place(x=480,y=100)

    heading = Label(frame,text="مرحبا دكتور اسامة",fg="black",bg="#ECF9FF",font=('Microsoft YaHei UI Light ',25,'bold'))
    heading.place(x=100,y=-6)


    def take_attendance():
        dataset_path ='\E:Haron\project'
        cap = cv2.VideoCapture(0)
        face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        new_member_name = input("Enter name of new member: ")
        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_detector.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.imshow('frame', frame)
            face_image = gray[y:y+h, x:x+w]
            resized_face = cv2.resize(face_image, (100, 100))
            cv2.imwrite(f"{dataset_path}/{new_member_name}.jpg", resized_face)
            print(f"New member {new_member_name} added to dataset.")
            break
        cap.release()
        cv2.destroyAllWindows()


    def add_new():
        print("Adding a new student...")

    def view_sheets():
        print("Viewing attendance sheets...")


    # create three buttons for taking attendance, adding new students, and viewing sheets
    attendance_button = Button(frame,width=15,border=0 ,bg="#0081C9",fg='white',text="Take Attendance", command=take_attendance, font=("Arial", 14))
    attendance_button.place(x=140,y=80)


    add_button = Button(frame, width=15,border=0,bg="#0081C9",fg='white',text="Add New", command=add_new, font=("Arial", 14))
    add_button.place(x=140,y=150)

    sheets_button = Button(frame,width=15,border=0 ,bg="#0081C9",fg='white',text="View Sheets", command=view_sheets, font=("Arial", 14))
    sheets_button.place(x=140,y=220)

    # start the main event loop to handle user interactions
    root.mainloop()