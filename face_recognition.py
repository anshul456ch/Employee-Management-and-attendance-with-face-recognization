from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import numpy as np
from abb import Employee
from train import Train

class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x732+0+0")
        self.root.title("Face Recognition System")

        # title
        title_lbl = Label(self.root, text="DETECT FACE", font=(
            "Roboto", 20, "bold"), bg="#102754", fg="#D4E8FF")
        title_lbl.place(x=0, y=0, width=1366, height=30)

        # first image
        first_top = Image.open(r"images\facerec8.jpg")
        first_top = first_top.resize((683, 730), Image.ANTIALIAS)
        self.photofirst_top = ImageTk.PhotoImage(first_top)

        f_lbl = Label(self.root, image=self.photofirst_top)
        f_lbl.place(x=0, y=30, width=683, height=730)

        # second image
        second_top = Image.open(r"images\facerec1.jpg")
        second_top = second_top.resize((683, 730), Image.ANTIALIAS)
        self.photosecond_top = ImageTk.PhotoImage(second_top)

        f_lbl = Label(self.root, image=self.photosecond_top)
        f_lbl.place(x=683, y=30, width=683, height=730)

        # face_detector frame
        face_detector_button_frame = Frame(self.root, bd=2,
                                           relief=RIDGE, bg="#FFFFFF")
        face_detector_button_frame.place(x=857, y=660, width=320, height=30)

        face_detector_button = Button(face_detector_button_frame,  text="FACE RECOGNITION", command=self.face_recog, width=39, font=(
            "Roboto", 10, "bold"), bg="#10544d", fg="#D4E8FF")
        face_detector_button.grid(row=0, column=0)

    def face_recog(self):
        def draw_boundray(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)
            coord = []
            for(x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
                id, predict = clf.predict(gray_image[y:y+h, x:x+w])
                confidence = int((100*(1-predict/300)))
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="#Ttls741", database="emfadb")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "select fname from employeetwo where employeeID="+str(id))
                n = my_cursor.fetchone()
                print(n)
                
                n = "+".join(str(n))
                my_cursor.execute(
                    "select employeeID from employeetwo where employeeID="+str(id))
                r = my_cursor.fetchone()
                r = "+".join(str(r))
                if confidence > 77:
                    cv2.putText(
                        img, f"Name:{n}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"ID:{r}", (x, y-30), cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown face", (x, y-5),cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 255), 3)
                coord = [x, y, w, h]
            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundray(img, faceCascade, 1.1,10, (255, 255, 255), "Face", clf)
            return img
        faceCascade = cv2.CascadeClassifier(
            "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.yml")
        video_cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        while True:
            ret, img = video_cap.read()
            img = recognize(img, clf, faceCascade)
            cv2.imshow("Welcome to face recognization", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        video_cap.release()
        cv2.destroyAllWindows()


# main
if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()
