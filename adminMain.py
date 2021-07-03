from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk


class Employee_Management_And_Attendance_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Management And Attendance System")

        # first image
        img = Image.open(r"images\firstImage.jpg")
        img = img.resize((450, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=450, height=130)

        # second image
        img1 = Image.open(r"images\secondImage.jpg")
        img1 = img1.resize((450, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=450, y=0, width=450, height=130)

        # third image
        img2 = Image.open(r"images\thirdImage.jpg")
        img2 = img2.resize((500, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=900, y=0, width=500, height=130)

        # background image
        img3 = Image.open(r"images\backgroundImage.jpg")
        img3 = img3.resize((1530, 710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(bg_img, text="Employee Management And Attendance System", font=(
            "Roboto", 32, "bold"), bg="#102754", fg="#D4E8FF")
        title_lbl.place(x=0, y=0, width=1400, height=45)

        # employee Button
        img4 = Image.open(r"images\employeeButtonImage.jpg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4, cursor="hand2")
        b1.place(x=100, y=80, width=220, height=220)

        b1_1 = Button(bg_img, text="Employee Details", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="#102754", fg="#D4E8FF")
        b1_1.place(x=100, y=280, width=220, height=40)

        # Detect face Button
        img5 = Image.open(r"images\detectFaceImage.jpg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, image=self.photoimg5, cursor="hand2")
        b1.place(x=400, y=80, width=220, height=220)

        b1_1 = Button(bg_img, text="Detect Face", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="#102754", fg="#D4E8FF")
        b1_1.place(x=400, y=280, width=220, height=40)

        # Attendance Button
        img6 = Image.open(r"images\attendanceButtonImage.jpg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b1.place(x=700, y=80, width=220, height=220)

        b1_1 = Button(bg_img, text="Attendance", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="#102754", fg="#D4E8FF")
        b1_1.place(x=700, y=280, width=220, height=40)

        # Admin Button
        img7 = Image.open(r"images\helpButtonImage.jpg")
        img7 = img7.resize((220, 220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b1.place(x=1020, y=80, width=220, height=220)

        b1_1 = Button(bg_img, text="Admin Panel", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="#102754", fg="#D4E8FF")
        b1_1.place(x=1020, y=280, width=220, height=40)

        # Train Button
        img8 = Image.open(r"images\trainButtonImage.jpg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, image=self.photoimg8, cursor="hand2")
        b1.place(x=100, y=350, width=220, height=220)

        b1_1 = Button(bg_img, text="Train Data", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="#102754", fg="#D4E8FF")
        b1_1.place(x=100, y=550, width=220, height=40)

        # Photos Button
        img9 = Image.open(r"images\photosImageButton.jpg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, image=self.photoimg9, cursor="hand2")
        b1.place(x=400, y=350, width=220, height=220)

        b1_1 = Button(bg_img, text="Photos", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="#102754", fg="#D4E8FF")
        b1_1.place(x=400, y=550, width=220, height=40)

        # Developers Button
        img10 = Image.open(r"images\devlopersButtonImage.jpg")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b1 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b1.place(x=700, y=350, width=220, height=220)

        b1_1 = Button(bg_img, text="Developers", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="#102754", fg="#D4E8FF")
        b1_1.place(x=700, y=550, width=220, height=40)

        # Exit Button
        img11 = Image.open(r"images\exitButtonImage.jpg")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b1 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b1.place(x=1020, y=350, width=220, height=220)

        b1_1 = Button(bg_img, text="Exit", cursor="hand2", font=(
            "times new roman", 15, "bold"), bg="#102754", fg="#D4E8FF")
        b1_1.place(x=1020, y=550, width=220, height=40)


if __name__ == "__main__":
    root = Tk()
    obj = Employee_Management_And_Attendance_System(root)
    root.mainloop()
