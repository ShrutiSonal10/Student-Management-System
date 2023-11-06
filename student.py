from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
# from PIL import Image.LANCZOS
# from PIL import Image.Resampling.LANCZOS
from tkinter import messagebox
import mysql.connector

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("4060x1590+0+0")
        self.root.title("face recognition system")


        # =============VARIABLES=============
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year= StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name= StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender= StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone= StringVar()
        self.var_address= StringVar()
        self.var_teacher= StringVar()

     #  first img
        img = Image.open(r"C:\Users\Shruti Sonal\Desktop\finalYear\college_image\student01.jpg")
        img = img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

    #   second image
        img1 = Image.open(r"C:\Users\Shruti Sonal\Desktop\finalYear\college_image\cllg.jpg")
        img1 = img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


    # 3rd image
        img2 = Image.open(r"C:\Users\Shruti Sonal\Desktop\finalYear\college_image\student02.jpg")
        img2 = img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
        
    # background image

        img3 = Image.open(r"C:\Users\Shruti Sonal\Desktop\finalYear\college_image\studentbg.jpg")
        img3 = img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)



        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        

        title_lbl = Label(bg_img,text = "STUDENT MANAGEMENT SYSTEM",font= ("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
        main_frame = Frame(bg_img,bd=2)
        main_frame.place(x=10,y=60,width=1400,height=550)
        # left label frame
        left_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=650,height=580)
       
        # left image
        img_left = Image.open(r"C:\Users\Shruti Sonal\Desktop\finalYear\college_image\student02.jpg")
        img_left = img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_left= ImageTk.PhotoImage(img_left)

        f_lbl = Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=715,height=130)
        # current course information
        
        current_course_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text=" Current Courses",font=("times new roman",12,"bold"))
        current_course_frame.place(x=10,y=140,width=650,height=130)

        dep_label = Label(current_course_frame,text="Department",font=("times new roman",10,"bold"))
        dep_label.grid(row=0,column=0)
        dep_combo = ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",10,"bold"),width=17, state="read only")
        dep_combo["values"]=("Select Department","Computer","IT","Electronics and Communication","Civil","Mechanical");
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=3)
        #courses
        course_label = Label(current_course_frame,text="Course",font=("times new roman",10,"bold"))
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        course_combo = ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",10,"bold"),width=17, state="readonly")
        course_combo["values"]=("Select Course","FE","SE","TE","BE");
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=3,sticky=W)

        #year
        year_label = Label(current_course_frame,text="Year",font=("times new roman",10,"bold"))
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        year_combo = ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",10,"bold"),width=17, state="readonly")
        year_combo["values"]=("Select year","2020-2021","2021-2022","2022-2023","2023-2024");
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=3,sticky=W)
        #semester
        semester_label = Label(current_course_frame,text="Semester",font=("times new roman",10,"bold"))
        semester_label.grid(row=1,column=2,padx=10,sticky=W)
        semester_combo = ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",10,"bold"),width=17, state="read only")
        semester_combo["values"]=("Select Semester","Semester-1","Semester-2");
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=3,sticky=W)
         # class student information
        
        class_student_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text=" Class Student Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=10,y=220,width=640,height=300)
        
          #student_name
        student_name_label = Label(class_student_frame,text="Student Name",font=("times new roman",10,"bold"))
        student_name_label.grid(row=0,column=0,padx=10,pady=3,sticky=W)
        student_name_entry= ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=20,font=("times new roman",10,"bold"))
        student_name_entry.grid(row=0,column=1,padx=10,pady=3,sticky=W)
          #rollnumber
        roll_label = Label(class_student_frame,text="Roll Number",font=("times new roman",10,"bold"))
        roll_label.grid(row=0,column=2,padx=10,pady=3,sticky=W)
        roll_entry= ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",10,"bold"))
        roll_entry.grid(row=0,column=3,padx=10,pady=3,sticky=W)
          #gender
        gender_label = Label(class_student_frame,text="Gender",font=("times new roman",10,"bold"))
        gender_label.grid(row=1,column=0,padx=10,pady=3,sticky=W)
        # gender_entry= ttk.Entry(class_student_frame,textvariable=self.var_gender,width=20,font=("times new roman",10,"bold"))
        # gender_entry.grid(row=1,column=1,padx=10,sticky=W)
        gender_combo = ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",10,"bold"),width=17, state="readonly")
        gender_combo["values"]=("Select gender","Male","Female","others")
        gender_combo.current(0)
        gender_combo.grid(row=1,column=1,padx=10,pady=3,sticky=W)

        #dob
        dob_label = Label(class_student_frame,text="DOB",font=("times new roman",10,"bold"))
        dob_label.grid(row=1,column=2,padx=10,pady=3,sticky=W)
        dob_entry= ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",10,"bold"))
        dob_entry.grid(row=1,column=3,padx=10,pady=3,sticky=W)
        #email
        email_label = Label(class_student_frame,text="Email",font=("times new roman",10,"bold"))
        email_label.grid(row=2,column=0,padx=10,pady=3,sticky=W)
        email_entry= ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",10,"bold"))
        email_entry.grid(row=2,column=1,padx=10,pady=3,sticky=W)
         #phone number
        phone_label = Label(class_student_frame,text="Phone no.",font=("times new roman",10,"bold"))
        phone_label.grid(row=2,column=2,padx=10,pady=3,sticky=W)
        phone_entry= ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",10,"bold"))
        phone_entry.grid(row=2,column=3,padx=10,pady=3,sticky=W)
        # address
      
        address_label = Label(class_student_frame,text="Address",font=("times new roman",10,"bold"))
        address_label.grid(row=3,column=0,padx=10,pady=3,sticky=W)
        address_entry= ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",10,"bold"))
        address_entry.grid(row=3,column=1,padx=10,pady=3,sticky=W)
        #Class div
         #student_id
        student_id_label = Label(class_student_frame,text="StudentID",font=("times new roman",10,"bold"))
        student_id_label.grid(row=3,column=2,padx=10,pady=3,sticky=W)
        student_id_entry= ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",10,"bold"))
        student_id_entry.grid(row=3,column=3,padx=10,pady=3,sticky=W)
        
         #teacher_name
        teacher_label = Label(class_student_frame,text="Teacher Name",font=("times new roman",10,"bold"))
        teacher_label.grid(row=4,column=0,padx=10,pady=3,sticky=W)
        teacher_entry= ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",10,"bold"))
        teacher_entry.grid(row=4,column=1,padx=10,pady=3,sticky=W)
        # radio button
        self.var_radio1=StringVar()
        radio_button1= ttk.Radiobutton(class_student_frame,text="Take Photo Sample",variable=self.var_radio1,value="yes")
        radio_button1.grid(row=5,column=0)
        radio_button2= ttk.Radiobutton(class_student_frame,text="No Photo Sample",variable=self.var_radio1,value="no")
        radio_button2.grid(row=5,column=1)
        # buttons frame
        btn_frame = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=130,width=700,height=35)
        # save button
        save_btn = Button(btn_frame,width=21,text="Save",command=self.add_data,font=("times new roman",10,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)
           # update button
        update_btn = Button(btn_frame,width=21,text="Update",command=self.update_data,font=("times new roman",10,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)
           # delete button
        delete_btn = Button(btn_frame,width=21,text="Delete",command = self.delete_data,font=("times new roman",10,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)
           # reset button
        reset_btn = Button(btn_frame,width=23,text="Reset",command = self.reset_data,font=("times new roman",10,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        
        btn_frame1 = Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame1.place(x=0,y=160,width=715,height=35)
           #take button
        Take_Photo_btn = Button(btn_frame1,width=40,text="Take Photo",font=("times new roman",10,"bold"),bg="blue",fg="white")
        Take_Photo_btn.grid(row=0,column=0)
           # update button
        Update_Photo_btn = Button(btn_frame1,width=50,text="Update Photo",font=("times new roman",10,"bold"),bg="blue",fg="white")
        Update_Photo_btn.grid(row=0,column=1)
         # right label frame
        right_frame = LabelFrame(main_frame,bd=2,relief=RIDGE,text="STUDENT DETAILS",font=("times new roman",12,"bold"))
        right_frame.place(x=680,y=10,width=650,height=580)
         # right image
        img_right = Image.open(r"C:\Users\Shruti Sonal\Desktop\finalYear\college_image\winx05.jpg")
        img_right = img_right.resize((720,210),Image.Resampling.LANCZOS)
        self.photoimg_right= ImageTk.PhotoImage(img_right)

        f_lbl = Label(right_frame,image=self.photoimg_right)
        f_lbl.place(x=5,y=0,width=715,height=130)
        # current course information
        #   ===================SEARCHING SYSTEM==============
        
         # class student information
        
        search_frame = LabelFrame(right_frame,bd=2,relief=RIDGE,text=" Search System",font=("times new roman",12,"bold"))
        search_frame.place(x=10,y=135,width=740,height=70)
        search_label = Label(search_frame,text="Search By",font=("times new roman",12,"bold"),bg="pink")
        search_label.grid(row=0,column = 0,padx=10,pady=5,sticky= W)
        search_combo = ttk.Combobox(search_frame,font=("times new roman",10,"bold"),width=17, state="read only")
        search_combo["values"]=("Select","Roll-no.","Phone no.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        # search box
        search_entry= ttk.Entry(search_frame,width=20,font=("times new roman",10,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=3,sticky=W)
        
            # search button
        search_btn = Button(search_frame,width=13,text="Search",font=("times new roman",10,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)
           # showall button
        showAll_btn = Button(search_frame,width=13,text="Show All",font=("times new roman",10,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)
        # ==========================TABLE FRAME=======================
        # table frame
        table_frame = Frame(right_frame,bd=2,relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=250)
        # scroll_bar
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text = "Department")
        
        self.student_table.heading("course", text = "Course")
        
        self.student_table.heading("year", text = "Year")
        
        self.student_table.heading("sem", text = "Semester")
        
        self.student_table.heading("id", text = "StudentID")
        
        self.student_table.heading("name", text = "StudentName")
        
        self.student_table.heading("div", text = "ClassDiv")
        
        self.student_table.heading("roll", text = "Roll")
        
        self.student_table.heading("gender", text = "Gender")
        
        self.student_table.heading("dob", text = "DOB")
         
        self.student_table.heading("email", text = "Email")
         
        self.student_table.heading("phone", text = "Phone")
        
        self.student_table.heading("address", text = "Address")
        
        self.student_table.heading("teacher", text = "Teacher")
        
        self.student_table.heading("photo", text = "Photo")
       
        self.student_table["show"]="headings"
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


        # ========================================FUNCTION DECLARATION=================================
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="mampi1004",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),self.var_course.get(),self.var_year.get(),self.var_semester.get(),self.var_std_id.get()
                    ,self.var_std_name.get(),self.var_div.get(),self.var_roll.get(),self.var_gender.get(),
                    self.var_dob.get(),self.var_email.get(),self.var_phone.get(),self.var_address.get(),self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)    
# =========================FETCH DATA===============================================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username="root",password="mampi1004",database="face_recognizer")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student ")
        data = my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()       
# ===========================GET CURSOR=======================================
    def get_cursor(self,event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data= content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

# ============================================UPDATE FUNCTION===========================================
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
                messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do you want to update this student details?", parent = self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="mampi1004",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("Update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Division=%s,Name=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                        
                                                                        self.var_dep.get(),
                                                                        self.var_course.get(),
                                                                        self.var_year.get(),
                                                                        self.var_semester.get(),
                                                                        self.var_div.get(),
                                                                        self.var_std_name.get(),
                                                                        self.var_roll.get(),
                                                                        self.var_gender.get(),
                                                                        self.var_dob.get(),
                                                                        self.var_email.get(),
                                                                        self.var_phone.get(),
                                                                        self.var_address.get(),
                                                                        self.var_teacher.get(),
                                                                        self.var_radio1.get(),
                                                                        self.var_std_id.get()
                                                                           ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root) 
                conn.commit()
                self.fetch_data()   
                conn.close()                                                       

            except Exception as es:
                messagebox.showerror("Error", f"Due to : {str(es)}", parent = self.root)

    # ===============================DELETE================================================
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student id is required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete page","Do you want to delete this student?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="mampi1004",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root)  


# ======================================RESET==============================================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")





                                           
        


        
  






















if __name__=="__main__":
    root = Tk()
    obj = Student(root)
    root.mainloop()