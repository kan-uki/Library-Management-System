from datetime import datetime
from tkinter import *
from tkinter import ttk,messagebox
import mysql.connector as con
from tkcalendar import DateEntry

def student_add():
    mycon=con.connect(host='localhost',user='root',passwd='cricket2004',database='cs_project')
    cur=mycon.cursor()

    r1 = Toplevel()
    r1.title("Add Student Details")
    r1.state('zoomed')

    #BACKGROUND IMAGE
    bg = PhotoImage(file = "leaf.png")
    img = Label(r1, image = bg,borderwidth=0)
    img.place(x = 0,y = 0)

    #LABELS
    lb1=Label(r1,text='ADD STUDENT DETAILS',fg='White',font = ("Comic Sans MS bold",35),padx=20,pady=10,borderwidth=3,relief='solid', bg = '#000080')
    lb1.place(x = 430, y = 55)

    lb2=Label(r1, bg='#A2242F',fg='White',text = "ENTER NAME:", font = ("Comic Sans MS bold",17),padx=20,pady=5,width=26)
    lb2.place(x = 280, y = 225)

    lb3=Label(r1, bg='#A2242F',fg='White',text = "ENTER DATE OF BIRTH:", font = ("Comic Sans MS bold",17),padx=20,pady=5,width=26)
    lb3.place(x = 280, y = 305)

    lb4=Label(r1, bg='#A2242F',fg='White',text = "ENTER ADMISSION NUMBER:", font = ("Comic Sans MS bold",17),padx=20,pady=5,width=26)
    lb4.place(x = 280, y = 385)

    lb5=Label(r1, bg='#A2242F',fg='White',text = "ENTER CLASS:", font = ("Comic Sans MS bold",17),padx=20,pady=5,width=26)
    lb5.place(x = 280, y = 465)

    lb6=Label(r1, bg='#A2242F',fg='White',text = "ENTER SECTION:", font = ("Comic Sans MS bold",17),padx=20,pady=5,width=26)
    lb6.place(x = 280, y = 545)

    #TEXT BOX
    t1=ttk.Entry(r1,width=30,font = ("Comic Sans MS bold",17))
    t1.place(x = 780, y = 225)

    cal = DateEntry(r1,date_pattern='dd/MM/yyyy',font = ("Comic Sans MS bold",18),state='readonly',background='darkblue',foreground='white')
    cal.place(x = 780, y = 305,width=424)

    t2=ttk.Entry(r1,width=30,font = ("Comic Sans MS bold",17))
    t2.place(x = 780, y = 385)

    dropdown=ttk.Combobox(r1,values=['Class','1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'], font = ("Comic Sans MS bold",17),state='readonly')
    dropdown.current(0)
    dropdown.place(x = 780, y = 465)
    dropdown.config(width = 29, height = 6)

    dropdown1=ttk.Combobox(r1,values=['Section','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'], font = ("Comic Sans MS bold",17),state='readonly')
    dropdown1.current(0)
    dropdown1.place(x = 780, y = 545)
    dropdown1.config(width = 29, height = 6)

    def add_button():
        name = t1.get().strip()

        dob = cal.get()
        dob=datetime.strptime(dob,'%d/%m/%Y')
        dob=dob.strftime('%Y/%m/%d')

        admin_no = t2.get().strip()
        clas=dropdown.get()
        section = dropdown1.get()

        if name=='' or admin_no=='':
            messagebox.showerror("ERROR","NO FIELD CAN BE EMPTY",parent=r1)
            t1.delete(0,END)
            t2.delete(0,END)
            dropdown.current(0)
            dropdown1.current(0)

        elif section=='Section':
            messagebox.showerror("ERROR","PLEASE SELECT SECTION",parent=r1)
            t1.delete(0,END)
            t2.delete(0,END)
            dropdown.current(0)
            dropdown1.current(0)

        elif clas=='Class':
            messagebox.showerror("ERROR","PLEASE SELECT CLASS",parent=r1)
            t1.delete(0,END)
            t2.delete(0,END)
            dropdown.current(0)
            dropdown1.current(0)

        else:
            cur.execute('select Admission_Number from student')
            l=cur.fetchall()
            flag=True
            for i in l:
                if i[0]==admin_no:
                    flag=False
            if flag==False:
                messagebox.showerror("ERROR","ADMISSION NUMBER ALREADY EXISTS",parent=r1)
                t1.delete(0,END)
                t2.delete(0,END)
            
            else:
                cur.execute('insert into student(Name, Date_Of_Birth, Admission_Number, Class, Section) values("{}","{}","{}","{}","{}")'.format(name,dob,admin_no,clas,section))       
                mycon.commit()
                messagebox.showinfo("SUCCESS","STUDENT DETAIL ADDED SUCCESSFULLY",parent=r1)
                t1.delete(0,END)
                t2.delete(0,END)
                dropdown.current(0)
                dropdown1.current(0)

    #BUTTONS
    btn1=Button(r1,text='ADD',fg='White',font = ("Comic Sans MS bold",20), bg = '#000080',padx=20,pady=5,borderwidth=3,relief='solid',width=12,command = add_button)
    btn1.place(y=675,x=410)

    btn2=Button(r1,text='GO BACK',fg='White',font = ("Comic Sans MS bold",20), bg = '#000080',padx=20,pady=5,borderwidth=3,relief='solid',width=12,command=r1.destroy)
    btn2.place(y=675,x=810)

    r1.mainloop()
