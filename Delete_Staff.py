from tkinter import *
import mysql.connector as con
from tkinter import ttk,messagebox

def staff_delete():
    mycon=con.connect(host='localhost',user='root',passwd='cricket2004',database='cs_project')
    cur=mycon.cursor()     

    r1=Toplevel()
    r1.title('Delete Staff Details')
    r1.state('zoomed')

    #BACKGROUND IMAGE
    bg = PhotoImage(file = "pinky.png")
    lbl1 = Label(r1, image = bg,borderwidth=0)
    lbl1.place(x = 0,y = 0)

    #LABELS
    lb1=Label(r1,text='DELETE STAFF DETAILS',font = ("Comic Sans MS bold",37),bg='#C71585',fg='white',padx=20,pady=10,borderwidth=3,relief='solid')
    lb1.place(x=420,y=60)

    lb2=Label(r1, bg='#FFB6C1',fg='White',text = "ENTER STAFF ID:", font = ("Comic Sans MS bold",24),pady=5,width=25)
    lb2.place(x = 210, y = 330)

    #TEXT BOXES
    t1=ttk.Entry(r1,width=24,font = ("Comic Sans MS bold",24))
    t1.place(x = 800, y = 330,height=55)

    def delete_button():
        
        staff_id=t1.get().strip()

        if staff_id=='':
                
                messagebox.showerror("ERROR","STAFF ID CANNOT BE EMPTY",parent=r1)

        else:
            cur.execute('select staffid from staff')
            
            l=cur.fetchall()

            if l!=None:
            
                for i in l:
            
                    if str(i[0])==staff_id:

                        cur.execute('delete from staff where staffid={}'.format(staff_id))
            
                        mycon.commit()
                
                        t1.delete(0,END)
                
                        messagebox.showinfo("SUCCESS","RECORD SUCCESSFULLY DELETED",parent=r1)

                        break

                else:
                    messagebox.showerror("ERROR","STAFF ID IS INCORRECT",parent=r1)

                    t1.delete(0,END)

            else:
            
                messagebox.showerror("ERROR","STAFF TABLE IS EMPTY",parent=r1)

                t1.delete(0,END)

    btn1=Button(r1,text='DELETE',font = ("Comic Sans MS bold",24),padx=40,fg='white',pady=5,bg='#C71585',borderwidth=3,relief='solid',command=delete_button)
    btn1.place(y=570,x=420)        

    btn2=Button(r1,text='GO BACK',font = ("Comic Sans MS bold",24),padx=40,pady=5,fg='white',borderwidth=3,bg='#C71585',relief='solid',command=r1.destroy)
    btn2.place(y=570,x=850)

    r1.mainloop()
