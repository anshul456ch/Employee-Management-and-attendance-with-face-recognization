from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np


class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x732+0+0")
        self.root.title("Face Recognition System")

     # title
        title_lbl = Label(self.root, text="TRAIN DATASET", font=(
            "Roboto", 20, "bold"), bg="#102754", fg="#D4E8FF")
        title_lbl.place(x=0, y=0, width=1366, height=30)
        # first image
        first_top = Image.open(r"images\train3.jpg")
        first_top = first_top.resize((452, 260), Image.ANTIALIAS)
        self.photofirst_top = ImageTk.PhotoImage(first_top)

        f_lbl = Label(self.root, image=self.photofirst_top)
        f_lbl.place(x=0, y=30, width=452, height=260)

        # second image
        second_top = Image.open(r"images\train5.jpg")
        second_top = second_top.resize((460, 260), Image.ANTIALIAS)
        self.photosecond_top = ImageTk.PhotoImage(second_top)

        f_lbl = Label(self.root, image=self.photosecond_top)
        f_lbl.place(x=452, y=30, width=460, height=260)

        # third image
        third_top = Image.open(r"images\train4.jpg")
        third_top = third_top.resize((454, 260), Image.ANTIALIAS)
        self.photothird_top = ImageTk.PhotoImage(third_top)

        f_lbl = Label(self.root, image=self.photothird_top)
        f_lbl.place(x=912, y=30, width=454, height=260)

        # first image
        first_middle = Image.open(r"images\mid2.jpg")
        first_middle = first_middle.resize((452, 220), Image.ANTIALIAS)
        self.photofirst_middle = ImageTk.PhotoImage(first_middle)

        f_lbl = Label(self.root, image=self.photofirst_middle)
        f_lbl.place(x=0, y=290, width=452, height=220)

        # second image
        second_middle = Image.open(r"images\col.png")
        second_middle = second_middle.resize((460, 220), Image.ANTIALIAS)
        self.photosecond_middle = ImageTk.PhotoImage(second_middle)

        f_lbl = Label(self.root, image=self.photosecond_middle)
        f_lbl.place(x=452, y=290, width=460, height=220)

        # train buttons frame
        train_button_frame = Frame(self.root, bd=2,
                                   relief=RIDGE, bg="#FFFFFF")
        train_button_frame.place(x=525, y=370, width=320, height=30)

        train_button = Button(train_button_frame, text="Train Dataset", command=self.train_classifier,  width=39, font=(
            "Roboto", 10, "bold"), bg="#10544d", fg="#D4E8FF")
        train_button.grid(row=0, column=0)

        # third image
        third_middle = Image.open(r"images\mid5.jpg")
        third_middle = third_middle.resize((454, 220), Image.ANTIALIAS)
        self.photothird_middle = ImageTk.PhotoImage(third_middle)

        f_lbl = Label(self.root, image=self.photothird_middle)
        f_lbl.place(x=912, y=290, width=454, height=220)

        # first image
        first_bottom = Image.open(r"images\train2.jpg")
        first_bottom = first_bottom.resize((452, 260), Image.ANTIALIAS)
        self.photofirst_bottom = ImageTk.PhotoImage(first_bottom)

        f_lbl = Label(self.root, image=self.photofirst_bottom)
        f_lbl.place(x=0, y=480, width=452, height=260)

        # second image
        second_bottom = Image.open(r"images\mid1.jpg")
        second_bottom = second_bottom.resize((460, 260), Image.ANTIALIAS)
        self.photosecond_bottom = ImageTk.PhotoImage(second_bottom)

        f_lbl = Label(self.root, image=self.photosecond_bottom)
        f_lbl.place(x=452, y=480, width=460, height=260)

        # third image
        third_bottom = Image.open(r"images\train7.jpg")
        third_bottom = third_bottom.resize((454, 260), Image.ANTIALIAS)
        self.photothird_bottom = ImageTk.PhotoImage(third_bottom)

        f_lbl = Label(self.root, image=self.photothird_bottom)
        f_lbl.place(x=912, y=480, width=454, height=260)

    # train
    def train_classifier(self):
        data_dir = ("dataset")
        path = [os.path.join(data_dir, file)for file in os.listdir(data_dir)]

        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert('L')  # grayscale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training Dataset", imageNp)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        # train classifier
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Dataset Completed")


# main
if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
