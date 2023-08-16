from tkinter import *
from datetime import *
import mysql.connector as con
import time
from tkinter import messagebox

def issue():
    
    mycon=con.connect(host='localhost',user='root',passwd='cricket2004',database='cs_project')
    
    cur=mycon.cursor(buffered=True)

    r1=Toplevel()
    
    r1.title('Issue')
    
    r1.state('zoomed')
    
    bg = PhotoImage(file = "newsunset.png")
    
    img = Label(r1, image = bg,borderwidth=0)
    
    img.place(x = 0,y = 0)

    #LABELS
    
    lb1=Label(r1,text='ISSUE BOOK',font = ("Comic Sans MS bold",40), bg='#C71585',fg='White',padx=20,pady=10,borderwidth=3,relief='solid')
    
    lb1.place(x=550,y=40)
    
    lb2=Label(r1, bg='#FF00FF',fg='White',text = "ENTER BOOK CODE:", font = ("Comic Sans MS bold",20),padx=42,pady=5,width=20)
    
    lb2.place(x=280,y=250)

    lb3=Label(r1, bg='#FF00FF',fg='White',text = "ENTER ADMISSION NUMBER:", font = ("Comic Sans MS bold",20),pady=5)
    
    lb3.place(x=280,y=400)

    #TEXT BOX

    t1=Entry(r1,width=26,font = ("Comic Sans MS bold",20),highlightcolor='blue',highlightthickness=4)

    t1.place(y=250,x=760)

    t2=Entry(r1,width=26,font = ("Comic Sans MS bold",20),highlightcolor='blue',highlightthickness=4)

    t2.place(y=400,x=760)

    #FUNCTIONS

    def issue_button():

        book_code=t1.get().strip()

        admn=t2.get().strip()

        if book_code=='' and admn=='':

            messagebox.showerror("ERROR","BOOK CODE AND ADMISSION NUMBER CANNOT BE EMPTY",parent=r1)

            t1.delete(0,END)

            t2.delete(0,END)

        elif book_code=='':

            messagebox.showerror("ERROR","BOOK CODE CANNOT BE EMPTY",parent=r1)

            t1.delete(0,END)

            t2.delete(0,END)

        elif admn=='':

            messagebox.showerror("ERROR","ADMISSION NUMBER CANNOT BE EMPTY",parent=r1)

            t1.delete(0,END)

            t2.delete(0,END)

        else:

            cur.execute('select Book_Code from books')

            flag1=False

            for i in cur.fetchall():

                if i[0]==book_code:

                    flag1=True

                    break

            cur.execute('select admission_number from student')

            flag2=False

            for i in cur.fetchall():

                if i[0]==admn:

                    flag2=True

                    break

            if flag1==False and flag2==False:

                messagebox.showerror("ERROR","BOOK CODE AND ADMISSION NUMBER NOT FOUND",parent=r1)

                t1.delete(0,END)

                t2.delete(0,END)

            elif flag1==False:

                messagebox.showerror("ERROR","BOOK CODE NOT FOUND",parent=r1)

                t1.delete(0,END)

            elif flag2==False:

                messagebox.showerror("ERROR","ADMISSION NUMBER NOT FOUND",parent=r1)

                t2.delete(0,END)

            else:

                cur.execute('select date_of_return from book_records where admission_number="{}"'.format(admn))

                l=cur.fetchone()

                if l!=None and l[0]==None:

                    messagebox.showerror("ERROR","YOU ALREADY HAVE ISSUED A BOOK",parent=r1)

                    t1.delete(0,END)

                    t2.delete(0,END)

                else:

                    cur.execute('select status from books where book_code="{}"'.format(book_code))

                    l1=cur.fetchone()

                    if l1[0]=='Issued':

                        messagebox.showerror("ERROR","BOOK HAS ALREADY BEEN ISSUED",parent=r1)

                        t1.delete(0,END)

                    else:

                        cur.execute('select name from student where admission_number="{}"'.format(admn))

                        student_name=cur.fetchone()[0]

                        cur.execute('select Name_of_book from books where book_code="{}"'.format(book_code))

                        book_name=cur.fetchone()[0]

                        date_of_issue=date.today().strftime("%Y/%m/%d")

                        due_date=(date.today()+timedelta(days=14)).strftime('%Y/%m/%d')

                        issuetime=time.strftime('%H:%M:%S')

                        cur.execute('insert into book_records(Name,Admission_number,book_name,book_code,date_of_issue,due_date,issue_time) values("{}","{}","{}","{}","{}","{}","{}")'.format(student_name,admn,book_name,book_code,date_of_issue,due_date,issuetime))

                        cur.execute('update books set status="Issued" where Book_code="{}"'.format(book_code))

                        mycon.commit()

                        due_date=datetime.strptime(due_date,'%Y/%m/%d')

                        messagebox.showinfo("SUCCESS","BOOK ISSUED SUCCESSFULY\n\nDUE DATE OF RETURN IS {}.".format(due_date.strftime('%d/%m/%Y')),parent=r1)

                        t1.delete(0,END)

                        t2.delete(0,END)

    #BUTTONS

    btn1=Button(r1,text='ISSUE',font = ("Comic Sans MS bold",20),width=11,pady=5,borderwidth=3, bg='#C71585',fg='White',command=issue_button)

    btn1.place(y=550,x=420)

    btn2=Button(r1,text='GO BACK',font = ("Comic Sans MS bold",20),width=11,pady=5,borderwidth=3, bg='#C71585',fg='White',command=r1.destroy)

    btn2.place(y=550,x=840)

    r1.mainloop()
