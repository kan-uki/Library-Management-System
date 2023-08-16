from tkinter import *
import mysql.connector as con
from tkinter import messagebox

def student_delete():
    mycon=con.connect(host='localhost',user='root',passwd='cricket2004',database='cs_project')
    cur=mycon.cursor()

    r1 = Toplevel()
    r1.title("Delete Student Details")
    r1.geometry('1080x720+200+35')
    r1.state('zoomed')

    bg = PhotoImage(file = "hogwarts.png")
    img = Label(r1, image = bg,borderwidth=0)
    img.place(x = 0,y = 0)

    lb1=Label(r1,text='DELETE STUDENT DETAILS',font = ("Comic Sans MS bold",35),bg = "#E0B589",padx=20,pady=10,borderwidth=3,relief='solid')
    lb1.place(x=400,y=60)

    lb2=Label(r1, bg='#798EA4',fg='White',text = "ENTER ADMISSION NUMBER:", font = ("Comic Sans MS bold",20),width=26,pady=5)
    lb2.place(x = 270, y = 330)

    #TEXT BOX
    t1=Entry(r1,width=26,font = ("Comic Sans MS bold",20),highlightcolor='blue',highlightthickness=4)
    t1.place(x = 800, y = 330)

    def delete_button():
        admin_no = t1.get().strip()

        if admin_no == "" :
            messagebox.showerror("ERROR","ADMISSION NUMBER CANNOT BE EMPTY",parent=r1)
            t1.delete(0,END)
        else:
            cur.execute("select Admission_Number from student")
            flag = False
            data = cur.fetchall()
            for i in data:
                if i[0] == admin_no:
                    flag = True
                    break

            if flag == False:
                messagebox.showerror("ERROR","ADMISSION NUMBER DOES NOT EXIST",parent=r1)
                t1.delete(0,END)
            else:
                cur.execute('select date_of_return from book_records where admission_number="{}"'.format(admin_no))
                l=cur.fetchall()
                flag=False

                if l!=[]:
                    for i in l:
                        if i[0]==None:
                            flag=True

                if flag==True:
                    messagebox.showerror("ERROR","STUDENT HAS A PENDING ISSUED BOOK",parent=r1)
                    t1.delete(0,END)

                else:
                    cur.execute("delete from student where Admission_Number = '{}' ".format(admin_no))
                    mycon.commit()
                    messagebox.showinfo("SUCCESS","STUDENT DETAIL DELETED SUCCESSFULLY",parent=r1)
                    t1.delete(0,END)

    btn1=Button(r1,text='DELETE',font = ("Comic Sans MS bold",20),bg = "#E0B589",padx=20,pady=5,borderwidth=3,relief='solid', command = delete_button)
    btn1.place(y=570,x=480)

    btn2=Button(r1,text='GO BACK',font = ("Comic Sans MS bold",20),bg = "#E0B589", padx=20,pady=5,borderwidth=3,relief='solid',command=r1.destroy)
    btn2.place(y=570,x=860)

    r1.mainloop()
