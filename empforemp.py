from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
#from tkcalendar import DateEntry
import re
import os
from mysql.connector import connect, Error


class Employee:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Employee Management And Attendance System")

        # callback function for validating user phone no

        def validate_phoneno(user_phoneno):
            if user_phoneno.isdigit():
                return True
            elif user_phoneno == "":
                return True
            else:
                messagebox.showinfo(
                    'Information', 'Only digits are allow for phone number')
                return False

        # validate salary
        def validate_salary(user_salary):
            if user_salary.isdigit():
                return True
            else:
                messagebox.showinfo(
                    'Information', 'Only digits are allow for Salary')
                return False

        # callback functtion for validating user email

        ######################
        # def callNewScreen():
        #	employee_info_frame.distroy()
        #	os.system('python eg3.py')

        ######################

        self.var_designation = StringVar()
        #self.var_designation_id = StringVar()
        self.var_emp_id = StringVar()
        self.var_emp_fname = StringVar()
        self.var_emp_lname = StringVar()
        self.var_email = StringVar()
        self.var_contact = StringVar()
        self.var_id_proff = StringVar()
        self.var_id_no = StringVar()
        self.var_salary = StringVar()
        self.var_street = StringVar()
        self.var_city = StringVar()
        self.var_state = StringVar()
        self.var_country = StringVar()
        self.var_gender = StringVar()
        self.var_take_photo = StringVar()
        self.var_dob = StringVar()

        

       # first image
        first = Image.open(r"images\stuFirstImage.jpg")
        first = first.resize((225, 100), Image.ANTIALIAS)
        self.photofirst = ImageTk.PhotoImage(first)

        f_lbl = Label(self.root, image=self.photofirst)
        f_lbl.place(x=0, y=0, width=225, height=100)

        # second image
        second = Image.open(r"images\stuSecondImage.jpg")
        second = second.resize((225, 100), Image.ANTIALIAS)
        self.photosecond = ImageTk.PhotoImage(second)

        f_lbl = Label(self.root, image=self.photosecond)
        f_lbl.place(x=225, y=0, width=225, height=100)

        # third image
        third = Image.open(r"images\stuThirdImage.jpg")
        third = third.resize((470, 100), Image.ANTIALIAS)
        self.photothird = ImageTk.PhotoImage(third)

        f_lbl = Label(self.root, image=self.photothird)
        f_lbl.place(x=450, y=0, width=470, height=100)

        # fourth image
        fourth = Image.open(r"images\stuFourthImage.jpg")
        fourth = fourth.resize((225, 100), Image.ANTIALIAS)
        self.photofourth = ImageTk.PhotoImage(fourth)

        f_lbl = Label(self.root, image=self.photofourth)
        f_lbl.place(x=920, y=0, width=225, height=100)

        # fifth image
        fifth = Image.open(r"images\stuFifthImage.jpg")
        fifth = fifth.resize((225, 100), Image.ANTIALIAS)
        self.photofifth = ImageTk.PhotoImage(fifth)

        f_lbl = Label(self.root, image=self.photofifth)
        f_lbl.place(x=1145, y=0, width=225, height=100)

        # background image
        background = Image.open(r"images\stubgImage.jpg")
        background = background.resize((1530, 710), Image.ANTIALIAS)
        self.photobackground = ImageTk.PhotoImage(background)

        bg_img = Label(self.root, image=self.photobackground)
        bg_img.place(x=0, y=100, width=1530, height=710)

        # title
        title_lbl = Label(bg_img, text="Employee Management And Attendance System", font=(
            "Roboto", 20, "bold"), bg="#102754", fg="#D4E8FF")
        title_lbl.place(x=0, y=0, width=1362, height=30)

        # main frame
        main_frame = Frame(bg_img, bd=2, bg="#FFFFFF")
        main_frame.place(x=5, y=36, width=1352, height=600)

        # left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="#FFFFFF", relief=RIDGE, font=("Roboto", 12, "bold")
                                )
        Left_frame.place(x=2, y=1, width=665, height=590)

        # title
        title_lbl = Label(Left_frame, text="Employee Details", font=(
            "Roboto", 20, "bold"), bg="#102754", fg="#D4E8FF")
        title_lbl.place(x=1, y=0, width=660, height=30)

        # left image
        img_left = Image.open(r"images\xyz.jpg")
        img_left = img_left.resize((660, 120), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=1, y=30, width=660, height=120)

        # employee information
        employee_info_frame = LabelFrame(Left_frame, bd=2, bg="#FFFFFF", relief=RIDGE,
                                         text="Employee Information ", font=("Roboto", 12, "bold"))
        employee_info_frame.place(x=1, y=150, width=658, height=435)

#######################################################
        # employeeId
        employeeId_label = Label(employee_info_frame,
                                 text="Employee ID :", font=("Roboto", 10, "bold"), bg="#FFFFFF")
        employeeId_label.grid(row=0, column=0, padx=10, pady=5, sticky=W)

        employeeId_entry = ttk.Entry(employee_info_frame, textvariable=self.var_emp_id,
                                     width=24, font=("Roboto", 10, "bold"))
        employeeId_entry.grid(row=0, column=1, padx=5, pady=5, sticky=W)

        # designationName
        designationName_label = Label(employee_info_frame,
                                      text="Designation :", font=("Roboto", 10, "bold"), bg="#FFFFFF")
        designationName_label.grid(row=0, column=2, padx=15, sticky=W)

        designationName_combo = ttk.Combobox(employee_info_frame,
                                             font=("Roboto", 10, "bold"), state="readonly", width=21)
        conn = mysql.connector.connect(
            host="localhost", username="root", password="#Ttls741", database="emfadb")
        my_cursor = conn.cursor()
        my_cursor.execute(
            "select title from designationone")
        row_designation = my_cursor.fetchall()

        designationName_combo = ttk.Combobox(employee_info_frame, textvariable=self.var_designation,
                                             font=("Roboto", 10, "bold"), state="readonly", width=21)
        designationName_combo["values"] = row_designation
        designationName_combo.current()
        designationName_combo.grid(row=0, column=3, padx=3, pady=10, sticky=W)

        # Name
        f_name_label = Label(employee_info_frame,
                             text="First Name :", font=("Roboto", 10, "bold"), bg="#FFFFFF")
        f_name_label.grid(row=1, column=0, padx=10, sticky=W)

        f_name_entry = ttk.Entry(employee_info_frame, textvariable=self.var_emp_fname,
                                 width=25, font=("Roboto", 10, "bold"))
        f_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

        # Name
        l_name_label = Label(employee_info_frame,
                             text="Last Name :", font=("Roboto", 10, "bold"), bg="#FFFFFF")
        l_name_label.grid(row=1, column=2, padx=10, sticky=W)

        l_name_entry = ttk.Entry(employee_info_frame, textvariable=self.var_emp_lname,
                                 width=25, font=("Roboto", 10, "bold"))
        l_name_entry.grid(row=1, column=3, padx=5, pady=5, sticky=W)

        # contactNo
        contactNo_label = Label(employee_info_frame,
                                text="Contact :", font=("Roboto", 10, "bold"), bg="#FFFFFF")
        contactNo_label.grid(row=2, column=0, padx=18, pady=5, sticky=W)

        contactNo_entry = ttk.Entry(employee_info_frame, textvariable=self.var_contact,
                                    width=24, font=("Roboto", 10, "bold"))
        contactNo_entry.grid(row=2, column=1, padx=2, pady=5, sticky=W)
        #############
        validate_phoneno = employee_info_frame.register(validate_phoneno)
        contactNo_entry.config(
            validate="key", validatecommand=(validate_phoneno, '%P'))
        ###############
        # email
        email_label = Label(employee_info_frame,
                            text="Email :", font=("Roboto", 10, "bold"), bg="#FFFFFF")
        email_label.grid(row=2, column=2, padx=10, pady=5, sticky=W)

        self.email_entry = ttk.Entry(employee_info_frame, textvariable=self.var_email,
                                     width=25, font=("Roboto", 10, "bold"))
        self.email_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        # idProff
        idProff_label = Label(employee_info_frame,
                              text="ID Proff :", font=("Roboto", 10, "bold"), bg="#FFFFFF")
        idProff_label.grid(row=3, column=0, padx=15, sticky=W)

        idProff_combo = ttk.Combobox(employee_info_frame, textvariable=self.var_id_proff,
                                     font=("Roboto", 10, "bold"), state="readonly", width=21)
        idProff_combo["values"] = (
            "Select ID Proff", "Aadhar Card", "PANCard", "Passport", "Driving Licence", "Voter ID")
        idProff_combo.current(0)
        idProff_combo.grid(row=3, column=1, padx=5, pady=10, sticky=W)

        # idNo
        idNo_label = Label(employee_info_frame,
                           text="ID No. :", font=("Roboto", 10, "bold"), bg="#FFFFFF")
        idNo_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        idNo_entry = ttk.Entry(employee_info_frame, textvariable=self.var_id_no,
                               width=25, font=("Roboto", 10, "bold"))
        idNo_entry.grid(row=3, column=3, padx=5, pady=5, sticky=W)

       # salary
        salary_label = Label(employee_info_frame,
                             text="Salary :", font=("Roboto", 10, "bold"), bg="#FFFFFF")
        salary_label.grid(row=4, column=0, padx=18, pady=5, sticky=W)

        salary_entry = ttk.Entry(employee_info_frame, textvariable=self.var_salary,
                                 width=24, font=("Roboto", 10, "bold"))
        salary_entry.grid(row=4, column=1, padx=2, pady=5, sticky=W)
        #############
        validate_salary = employee_info_frame.register(validate_salary)
        salary_entry.config(
            validate="key", validatecommand=(validate_salary, '%P'))
        ###############

        # dob
        dob_label = Label(employee_info_frame,
                          text="DOB (dd/mm/yy) :", font=("Roboto", 10, "bold"), bg="#FFFFFF")
        dob_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        # email_entry = ttk.Entry(employee_info_frame,
        # width=25, font=("Roboto", 10, "bold"))
        #email_entry.grid(row=2, column=3, padx=5, pady=5, sticky=W)

        dob_entry = ttk.Entry(employee_info_frame, width=24, textvariable=self.var_dob,
                              font=("Roboto", 10, "bold"))
        dob_entry.grid(row=4, column=3, padx=5, pady=5, sticky=W)

        # gender frame
        gender_frame = Frame(employee_info_frame, bd=2,
                             relief=RIDGE, bg="#FFFFFF")
        gender_frame.place(x=15, y=190, width=280, height=50)

        gender_label = Label(gender_frame, text="Gender :",
                             font=("Roboto", 10, "bold"), bg="#FFFFFF")
        gender_label.grid(row=0, column=0, padx=30, pady=10, sticky=W)

        male_radio = ttk.Radiobutton(
            gender_frame, variable=self.var_gender, text="Male", value="M")
        male_radio.grid(row=0, column=1, padx=5)

        female_radio = ttk.Radiobutton(
            gender_frame, variable=self.var_gender, text="Female", value="F")
        female_radio.grid(row=0, column=2, padx=5)

        # takePhoto frame
        take_photo_frame = Frame(employee_info_frame, bd=2,
                                 relief=RIDGE, bg="#FFFFFF")
        take_photo_frame.place(x=15, y=260, width=280, height=50)

        # take_photo button
        take_photo_button_label = Label(take_photo_frame,
                                        text="Take Photo :", font=("Roboto", 10, "bold"), bg="#FFFFFF")
        take_photo_button_label.grid(
            row=0, column=0, padx=30, pady=10, sticky=W)

        yes_radio = ttk.Radiobutton(
            take_photo_frame, variable=self.var_take_photo, text="Yes", value="Yes")
        yes_radio.grid(row=0, column=1, padx=5)

        no_radio = ttk.Radiobutton(
            take_photo_frame, variable=self.var_take_photo, text="No", value="No")
        no_radio.grid(row=0, column=2, padx=5)

        # address frame
        address_frame = LabelFrame(employee_info_frame, bd=2, bg="#FFFFFF", relief=RIDGE,
                                   text="Address", font=("Roboto", 12, "bold"))
        address_frame.place(x=310, y=190, width=295, height=130)

        # street
        street_label = Label(address_frame,
                             text="House No,Street :", font=("Roboto", 10, "bold"), bg="#FFFFFF")
        street_label.grid(row=0, column=0, padx=10, pady=2, sticky=W)

        street_entry = ttk.Entry(address_frame, textvariable=self.var_street,
                                 width=20, font=("Roboto", 10, "bold"))
        street_entry.grid(row=0, column=1, padx=5, pady=2, sticky=W)

        # city
        city_label = Label(address_frame,
                           text="City,Zipcode :", font=("Roboto", 10, "bold"), bg="#FFFFFF")
        city_label.grid(row=1, column=0, padx=10, pady=2, sticky=W)

        city_entry = ttk.Entry(address_frame, textvariable=self.var_city,
                               width=20, font=("Roboto", 10, "bold"))
        city_entry.grid(row=1, column=1, padx=5, pady=2, sticky=W)

        # state
        state_label = Label(address_frame,
                            text="State :", font=("Roboto", 10, "bold"), bg="#FFFFFF")
        state_label.grid(row=2, column=0, padx=10, pady=2, sticky=W)

        state_entry = ttk.Entry(address_frame, textvariable=self.var_state,
                                width=20, font=("Roboto", 10, "bold"))
        state_entry.grid(row=2, column=1, padx=5, pady=2, sticky=W)

        # country
        country_label = Label(address_frame,
                              text="Country :", font=("Roboto", 10, "bold"), bg="#FFFFFF")
        country_label.grid(row=3, column=0, padx=10, pady=2, sticky=W)

        country_entry = ttk.Entry(address_frame, textvariable=self.var_country,
                                  width=20, font=("Roboto", 10, "bold"))
        country_entry.grid(row=3, column=1, padx=5, pady=2, sticky=W)

       #########################################################

        # buttons frame
        button_frame = Frame(employee_info_frame, bd=2,
                             relief=RIDGE, bg="#FFFFFF")
        button_frame.place(x=1, y=328, width=652, height=90)

        save_button = Button(button_frame, command=self.add_employee, text="Save", width=39, font=(
            "Roboto", 10, "bold"), bg="#102754", fg="#D4E8FF")
        save_button.grid(row=0, column=0)

        update_button = Button(button_frame, command=self.employee_update, text="Update", width=39, font=(
            "Roboto", 10, "bold"), bg="#102754", fg="#D4E8FF")
        update_button.grid(row=0, column=1)

        delete_button = Button(button_frame, command=self.employee_delete, text="Delete", width=39, font=(
            "Roboto", 10, "bold"), bg="#102754", fg="#D4E8FF")
        delete_button.grid(row=1, column=0)

        reset_button = Button(button_frame, command=self.employee_reset, text="Reset", width=39, font=(
            "Roboto", 10, "bold"), bg="#102754", fg="#D4E8FF")
        reset_button.grid(row=1, column=1)

        # buttons frame

        self.take_photo_button = Button(button_frame, text="Take Photo Sample", width=39, padx=2, font=(
            "Roboto", 10, "bold"), bg="#102754", fg="#D4E8FF")
        self.take_photo_button.grid(row=2, column=0)

        self.update_photo_button = Button(button_frame, text="Update Photo Sample", width=39, font=(
            "Roboto", 10, "bold"), bg="#102754", fg="#D4E8FF")
        self.update_photo_button.grid(row=2, column=1)

        # right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="#FFFFFF", relief=RIDGE,
                                 font=("Roboto", 12, "bold"))
        Right_frame.place(x=680, y=1, width=665, height=590)

        # title
        title_lbl = Label(Right_frame, text="Search Employee Details", font=(
            "Roboto", 20, "bold"), bg="#102754", fg="#D4E8FF")
        title_lbl.place(x=1, y=0, width=660, height=30)

        # search
        search_frame = LabelFrame(Right_frame, bd=2, bg="#FFFFFF", relief=RIDGE,
                                  text="View Employee Details & Search System", font=("Roboto", 12, "bold"))
        search_frame.place(x=1, y=30, width=660, height=60)

        search_label = Label(search_frame,
                             text="Search By", font=("Roboto", 10, "bold"), bg="#102754", fg="#D4E8FF")
        search_label.grid(row=0, column=0, padx=5, pady=5, sticky=W)

        search_combo = ttk.Combobox(search_frame,
                                    font=("Roboto", 10, "bold"), state="readonly", width=15)
        search_combo["values"] = ("Id", "Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=2, pady=5, sticky=W)

        search_entry = ttk.Entry(search_frame,
                                 width=26, font=("Roboto", 10, "bold"))
        search_entry.grid(row=0, column=2, padx=2, pady=5, sticky=W)

        search_button = Button(search_frame, text="Search", width=14, padx=2, font=(
            "Roboto", 10, "bold"), bg="#102754", fg="#D4E8FF")
        search_button.grid(row=0, column=3, padx=2, pady=5, sticky=W)

        search_button1 = Button(search_frame, text="Show All", width=14, font=(
            "Roboto", 10, "bold"), bg="#102754", fg="#D4E8FF")
        search_button1.grid(row=0, column=4, padx=2, pady=2, sticky=W)

        # table
        table_frame = Frame(Right_frame, bd=2, bg="#FFFFFF", relief=RIDGE
                            )
        table_frame.place(x=1, y=90, width=660, height=500)

        # scrollBar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.employee_table = ttk.Treeview(table_frame, column=("emp_id", "desig_name", "emp_fname", "emp_lname",  "contact_no", "email_id", "id_proff", "id_no", "salary",  "dob", "gender",
                                                                "houseno_street", "zipcode_city", "state", "country", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)

        self.employee_table.heading("emp_id", text="Employee ID")
        #self.employee_table.heading("desig_id", text="Designation ID")
        self.employee_table.heading("desig_name", text="Designation")
        # self.employee_table.heading("is_indian", text="Is Indian")
        self.employee_table.heading("emp_fname", text="First Name")
        self.employee_table.heading("emp_lname", text="Last Name")
        #self.employee_table.heading("last_name", text="Last Name")
        self.employee_table.heading("contact_no", text="Contact No.")
        self.employee_table.heading("email_id", text="Email")
        self.employee_table.heading("id_proff", text="ID Proff")
        self.employee_table.heading("id_no", text="ID No.")
        self.employee_table.heading("gender", text="Gender")
        self.employee_table.heading("dob", text="DOB")
        self.employee_table.heading("houseno_street", text="House No ,Street")
        self.employee_table.heading("zipcode_city", text="City,Zipcode ")
        self.employee_table.heading("state", text="State")
        self.employee_table.heading("country", text="Country")
        self.employee_table.heading("salary", text="Salary")

        self.employee_table.heading("photo", text="Photo Sample")

        self.employee_table["show"] = "headings"

        #self.employee_table.column("desig_id", width=120)
        self.employee_table.column("emp_id", width=100)
        self.employee_table.column("desig_name", width=120)
        # self.employee_table.column("is_indian", width=100)
        self.employee_table.column("emp_fname", width=100)
        self.employee_table.column("emp_lname", width=100)
        #self.employee_table.column("last_name", width=100)
        self.employee_table.column("contact_no", width=120)
        self.employee_table.column("email_id", width=150)
        self.employee_table.column("id_proff", width=120)
        self.employee_table.column("id_no", width=120)
        self.employee_table.column("gender", width=70)
        self.employee_table.column("dob", width=100)
        self.employee_table.column("houseno_street", width=150)
        self.employee_table.column("zipcode_city", width=150)
        self.employee_table.column("state", width=150)
        self.employee_table.column("country", width=120)
        self.employee_table.column("salary", width=100)
        self.employee_table.column("photo", width=100)

        self.employee_table.pack(fill=BOTH, expand=1)
        self.employee_table.bind("<ButtonRelease>", self.employee_get_cursor)
        self.fetch_employee()

        

    def add_employee(self):
        # def isValidEmail(user_email):
        #   if len(user_email) > 7:
        #      if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0,9]{1,3})(]?)$", user_email) != None:
        #         return True
        #    return False
        # else:
        #   messagebox.showerror(
        #       'Error', 'This is not a valid email')
        # return False

        if self.var_emp_fname.get() == "" or self.var_designation.get() == "" or self.var_emp_lname.get() == "" or self.var_contact.get() == "" or self.var_email.get() == "" or self.var_id_proff.get() == "Select ID Proff" or self.var_id_no.get() == "" or self.var_gender.get() == "" or self.var_salary.get() == "" or self.var_take_photo.get() == "" or self.var_street.get() == "" or self.var_city.get() == "" or self.var_state.get() == "" or self.var_country.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        elif len(self.var_contact.get()) != 10:
            messagebox.showerror(
                "Error", "Mobile Number should be of 10 digits", parent=self.root)

   #     elif len(self.var_email.get()) > 7:
  #          if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0,9]{1,3})(]?)$", self.var_email) != None:
 #               return True
#            else:
    #            messagebox.showerror('Error', 'This is not a  valid email')
            # return False

        # elif self.var_email.get() != "":
          #   status = isValidEmail(self.var_email.get())
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="#Ttls741", database="emfadb")
                my_cursor = conn.cursor()
                abcd = "insert into employeetwo (fname,lname,contact,email,idProff,idNo,salary,gender,dob,street,city,state,country,takePhoto,designationTitle )  values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (self.var_emp_fname.get(), self.var_emp_lname.get(), self.var_contact.get(), self.var_email.get(
                ), self.var_id_proff.get(), self.var_id_no.get(), self.var_salary.get(), self.var_gender.get(), self.var_dob.get(), self.var_street.get(), self.var_city.get(), self.var_state.get(), self.var_country.get(), self.var_take_photo.get(), self.var_designation.get())
                print(abcd)
                my_cursor.execute(abcd)
                conn.commit()
                self.fetch_employee()
                conn.close()
                messagebox.showinfo(
                    "Success", "Employee details has been added successfully", parent=self.root)

            except Error as error:
                print(f"Error message :{error.msg}")
                print(f"Error number :{error.errno}")
                print(f"Sql State :{error.sqlstate}")

      # fetch data

    def fetch_employee(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="#Ttls741", database="emfadb")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from employeetwo")
        emp_data = my_cursor.fetchall()

        if len(emp_data) != 0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in emp_data:
                self.employee_table.insert("", END, values=i)
            conn.commit()
        conn.close()

 # get cursor

    def employee_get_cursor(self, event=""):
        cursor_focus = self.employee_table.focus()
        content = self.employee_table.item(cursor_focus)
        data = content["values"]

        self.var_emp_id.set(data[0])
        self.var_designation.set(data[1])
        self.var_emp_fname.set(data[2])
        self.var_emp_lname.set(data[3])
        self.var_contact.set(data[4])
        self.var_email.set(data[5])
        self.var_id_proff.set(data[6])
        self.var_id_no.set(data[7])
        self.var_salary.set(data[8])
        self.var_dob.set(data[9])
        self.var_gender.set(data[10])
        self.var_street.set(data[11])
        self.var_city.set(data[12])
        self.var_state.set(data[13])
        self.var_country.set(data[14])
        self.var_take_photo.set(data[15])

    # update employee

    def employee_update(self):
        if self.var_emp_fname.get() == "" or self.var_designation.get() == "" or self.var_emp_lname.get() == "" or self.var_contact.get() == "" or self.var_email.get() == "" or self.var_id_proff.get() == "Select ID Proff" or self.var_id_no.get() == "" or self.var_gender.get() == "" or self.var_salary.get() == "" or self.var_take_photo.get() == "" or self.var_street.get() == "" or self.var_city.get() == "" or self.var_state.get() == "" or self.var_country.get() == "":
            messagebox.showerror(
                "Error", "All Fields are required", parent=self.root)
        elif len(self.var_contact.get()) != 10:
            messagebox.showerror(
                "Error", "Mobile Number should be of 10 digits", parent=self.root)
        else:
            try:
                Update = messagebox.askyesno(
                    "Update", "Do you want to update this employee details", parent=self.root)
                if Update > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="#Ttls741", database="emfadb")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update employeetwo set designationtitle=%s,fname=%s,lname=%s,contact=%s,email=%s,idProff=%s,idNo=%s,salary=%s,dob=%s,gender=%s,street=%s,city=%s,state=%s,country=%s,takePhoto=%s where employeeID=%s", (self.var_designation.get(), self.var_emp_fname.get(), self.var_emp_lname.get(), self.var_contact.get(), self.var_email.get(
                    ), self.var_id_proff.get(), self.var_id_no.get(), self.var_salary.get(), self.var_dob.get(), self.var_gender.get(), self.var_street.get(), self.var_city.get(), self.var_state.get(), self.var_country.get(), self.var_take_photo.get(), self.var_emp_id.get()))
                else:
                    if not Update:
                        return
                messagebox.showinfo(
                    "Success", "Employee details successfully updated", parent=self.root)
                conn.commit()
                # self.fetch_data()
                self.fetch_employee()
                conn.close()
            except Error as error:
                print(f"Error message :{error.msg}")
                print(f"Error number :{error.errno}")
                print(f"Sql State :{error.sqlstate}")

    def employee_delete(self):
        if self.var_emp_id.get() == "":
            messagebox.showerror(
                "Error", "Employee id must be required", parent=self.root)
        else:
            try:
                delete = messagebox.askyesno(
                    "Delete employee", "Do you want to delete this employee", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="#Ttls741", database="emfadb")
                    my_cursor = conn.cursor()
                    sql = "delete from employeetwo where employeeID=%s"
                    val = (self.var_emp_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_employee()
                conn.close()
                messagebox.showinfo(
                    "Delete", "Successfully deleted employee details", parent=self.root)
            except Error as error:
                print(f"Error message :{error.msg}")
                print(f"Error number :{error.errno}")
                print(f"Sql State :{error.sqlstate}")

    # reset

    def employee_reset(self):
        self.var_emp_id.set("")
        self.var_designation.set("")
        self.var_emp_fname.set("")
        self.var_emp_lname.set("")
        self.var_contact.set("")
        self.var_email.set("")
        self.var_id_proff.set("Select ID Proff")
        self.var_id_no.set("")
        self.var_salary.set("")
        self.var_dob.set("")
        self.var_gender.set("")
        self.var_street.set("")
        self.var_city.set("")
        self.var_state.set("")
        self.var_country.set("")
        self.var_take_photo.set("")


if __name__ == "__main__":
    root = Tk()
    obj = Employee(root)
    root.mainloop()
