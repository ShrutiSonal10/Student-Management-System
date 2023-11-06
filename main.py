from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from student import Student
# from PIL import Image.LANCZOS
# from PIL import Image.Resampling.LANCZOS

class Face_Recognisation_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("4060x1590+0+0")
        self.root.title("face recognition system")
        #  first img
        img = Image.open(r"C:\Users\Shruti Sonal\Desktop\finalYear\college_image\ai.jpg")
        img = img.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

    #   second image
        img1 = Image.open(r"C:\Users\Shruti Sonal\Desktop\finalYear\college_image\face-rec-tech.png")
        img1 = img1.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)


    # 3rd image
        img2 = Image.open(r"C:\Users\Shruti Sonal\Desktop\finalYear\college_image\univ.jpg")
        img2 = img2.resize((500,130),Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
        
    # background image

        img3 = Image.open(r"C:\Users\Shruti Sonal\Desktop\finalYear\college_image\lux.jpg")
        img3 = img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)



        bg_img = Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)
        

        title_lbl = Label(bg_img,text = "FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",font= ("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)
    
        #student button
        img4 = Image.open(r"C:\Users\Shruti Sonal\Desktop\finalYear\college_image\student.jpg")
        img4 = img4.resize((500,220),Image.Resampling.LANCZOS)
        self.photoimg4= ImageTk.PhotoImage(img4)

        b1 = Button(bg_img,image = self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height = 220)

        b1_1 = Button(bg_img,text = "Students Details",command=self.student_details,cursor="hand2",font= ("times new roman",15,"bold"),
        bg="blue",fg="white")
        b1_1.place(x=200,y=300,width=220,height = 40)
        #detect face button
        img5 = Image.open(r"C:\Users\Shruti Sonal\Desktop\finalYear\college_image\detectFace.webp")
        img5 = img5.resize((200,220),Image.Resampling.LANCZOS)
        self.photoimg5= ImageTk.PhotoImage(img5)

        b2 = Button(bg_img,image = self.photoimg5,cursor="hand2")
        b2.place(x=500,y=100,width=220,height = 220)

        b2_2 = Button(bg_img,text = "Detect Face",cursor="hand2",font= ("times new roman",15,"bold"),
        bg="blue",fg="white")
        b2_2.place(x=500,y=300,width=220,height = 40)
         #attendance face button
        img6 = Image.open(r"C:\Users\Shruti Sonal\Desktop\finalYear\college_image\attendance.webp")
        img6 = img6.resize((500,220),Image.Resampling.LANCZOS)
        self.photoimg6= ImageTk.PhotoImage(img6)

        b3 = Button(bg_img,image = self.photoimg6,cursor="hand2")
        b3.place(x=800,y=100,width=220,height = 220)

        b3_3 = Button(bg_img,text = "Take Attendance",cursor="hand2",font= ("times new roman",15,"bold"),
        bg="blue",fg="white")
        b3_3.place(x=800,y=300,width=220,height = 40)
          #help_desk button
        img7 = Image.open(r"C:\Users\Shruti Sonal\Desktop\finalYear\college_image\attendance.webp")
        img7 = img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7= ImageTk.PhotoImage(img7)

        b4_4 = Button(bg_img,image = self.photoimg7,cursor="hand2")
        b4_4.place(x=1100,y=100,width=220,height = 220)

        b4_4 = Button(bg_img,text = "Help Desk",cursor="hand2",font= ("times new roman",15,"bold"),
        bg="blue",fg="white")
        b4_4.place(x=1100,y=300,width=220,height = 40)
          #train model button
        img8 = Image.open(r"C:\Users\Shruti Sonal\Desktop\finalYear\college_image\train_model.jpg")
        img8 = img8.resize((500,220),Image.Resampling.LANCZOS)
        self.photoimg8= ImageTk.PhotoImage(img8)

        b5_5 = Button(bg_img,image = self.photoimg8,cursor="hand2")
        b5_5.place(x=200,y=350,width=220,height = 220)

        b5_5 = Button(bg_img,text = "Train Model",cursor="hand2",font= ("times new roman",15,"bold"),
        bg="blue",fg="white")
        b5_5.place(x=200,y=350,width=220,height = 40)
        #developer button
        img9 = Image.open(r"C:\Users\Shruti Sonal\Desktop\finalYear\college_image\developer.webp")
        img9 = img9.resize((500,220),Image.Resampling.LANCZOS)
        self.photoimg9= ImageTk.PhotoImage(img9)

        b6_6 = Button(bg_img,image = self.photoimg9,cursor="hand2")
        b6_6.place(x=500,y=350,width=220,height = 220)

        b6_6 = Button(bg_img,text = "Developer",cursor="hand2",font= ("times new roman",15,"bold"),
        bg="blue",fg="white")
        b6_6.place(x=500,y=350,width=220,height = 40)
        #photo face button
        img10 = Image.open(r"C:\Users\Shruti Sonal\Desktop\finalYear\college_image\developer.webp")
        img10 = img10.resize((500,220),Image.Resampling.LANCZOS)
        self.photoimg10= ImageTk.PhotoImage(img10)

        b7_7 = Button(bg_img,image = self.photoimg8,cursor="hand2")
        b7_7.place(x=800,y=350,width=220,height = 220)

        b7_7 = Button(bg_img,text = "Photo Face",cursor="hand2",font= ("times new roman",15,"bold"),
        bg="blue",fg="white")
        b7_7.place(x=800,y=350,width=220,height = 40)
        #exit button
        img11 = Image.open(r"C:\Users\Shruti Sonal\Desktop\finalYear\college_image\developer.webp")
        img11 = img11.resize((500,220),Image.Resampling.LANCZOS)
        self.photoimg11= ImageTk.PhotoImage(img11)

        b8_8 = Button(bg_img,image = self.photoimg8,cursor="hand2")
        b8_8.place(x=1100,y=350,width=220,height = 220)

        b8_8 = Button(bg_img,text = "Exit",cursor="hand2",font= ("times new roman",15,"bold"),
        bg="blue",fg="white")
        b8_8.place(x=1100,y=350,width=220,height = 40)
# ======================function=========================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


         


if __name__=="__main__":
    root = Tk()
    obj = Face_Recognisation_System(root)
    root.mainloop()
