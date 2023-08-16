from tkinter import *
from datetime import *
import mysql.connector as con
from tkinter import messagebox

def return_book():
    
    mycon=con.connect(host='localhost',user='root',passwd='cricket2004',database='cs_project')
    
    cur=mycon.cursor()

    r1=Toplevel()    
    
    r1.title('RETURN')
    
    r1.state('zoomed')

    #Background Image
    
    bg = PhotoImage(file = "field.png")
    
    img = Label(r1, image = bg,borderwidth=0)
    
    img.place(x = 0,y = 0)

    #LABELS
    
    lb1=Label(r1,text='RETURN BOOK',font = ("Comic Sans MS bold",40),padx=20,pady=10,borderwidth=3,relief='solid',bg='orange',fg='black')
    
    lb1.place(x=540,y=40)
    
    lb2=Label(r1,bg='#FFD700',fg='black',text = "ENTER ADMISSION NUMBER:", font = ("Comic Sans MS bold",20),width=25,pady=5)
    
    lb2.place(x=270,y=330)

    #TEXT BOX
    
    t1=Entry(r1,width=25,font = ("Comic Sans MS bold",20),highlightcolor='blue',highlightthickness=4)
    
    t1.place(x=820,y=330)

    #FUNCTIONS
    
    def return_button():
    
        admn=t1.get().strip()

        if admn=='':
    
            messagebox.showerror("ERROR","ADMISSION NUMBER CANNOT BE EMPTY",parent=r1)
    
            t1.delete(0,END)

        else:
    
            cur.execute('select admission_number from student')

            for i in cur.fetchall():
    
                if i[0]==admn:

                    flag3=False
    
                    cur.execute('select date_of_return from book_records where admission_number="{}"'.format(admn))
        
                    l=cur.fetchall()

                    for i in range(len(l)):
        
                        if l==None or l[i][0]!=None:
        
                            pass
        
                        elif l[i][0]==None:
        
                            flag3=True
        
                            break

                    if flag3==False:
        
                        messagebox.showerror("ERROR","YOU HAVE NOT ISSUED ANY BOOK",parent=r1)
        
                        t1.delete(0,END)

                    elif flag3==True:
        
                            cur.execute('select book_code from book_records where admission_number="{}" and date_of_return is Null'.format(admn))
        
                            book_code=cur.fetchall()[0][0]
        
                            date_of_return=date.today().strftime("%Y/%m/%d")
        
                            cur.execute('update books set status="Not Issued" where Book_code="{}"'.format(book_code))
        
                            cur.execute('update book_records set date_of_return="{}" where admission_number="{}" and date_of_return is Null'.format(date_of_return,admn))
        
                            mycon.commit()

                            messagebox.showinfo("SUCCESS","BOOK RETURNED SUCCESSFULY",parent=r1)
        
                            t1.delete(0,END)
    
                    break

            else:
    
                messagebox.showerror("ERROR","ADMISSION NUMBER NOT FOUND",parent=r1)
    
                t1.delete(0,END)

            
    
                

    #BUTTONS
    
    btn1=Button(r1,text='RETURN',font = ("Comic Sans MS bold",25),width=15,pady=5,borderwidth=3,bg='orange',fg='black',command=return_button)
    
    btn1.place(y=600,x=340)

    btn2=Button(r1,text='GO BACK',font = ("Comic Sans MS bold",25),width=15,pady=5,borderwidth=3,bg='orange',fg='black',command=r1.destroy)
    
    btn2.place(y=600,x=870)

    r1.mainloop()
