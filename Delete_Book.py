from tkinter import *
from tkinter import ttk
import mysql.connector as con
from tkinter import messagebox

def book_delete():
    mycon=con.connect(host='localhost',user='root',passwd='cricket2004',database='cs_project')
    cur=mycon.cursor()

    root=Toplevel()
    root.title('Delete Books')
    root.state('zoomed')

    #BACKGROUND IMAGE
    bg = PhotoImage(file = "Aurora.png")
    lbl1 = Label(root, image = bg,borderwidth=0)
    lbl1.place(x = 0,y = 0)

    #LABELS
    lb1=Label(root,text='DELETE BOOKS',font = ("Comic Sans MS bold",40),bg='#C1A7C8',fg='#041926',padx=20,pady=10,borderwidth=3,relief='solid')
    lb1.place(x=540,y=60)

    lb2=Label(root, bg='#4179A7',fg='White',text = "ENTER BOOK CODE:", font = ("Comic Sans MS bold",24),pady=5,width=25)
    lb2.place(x = 210, y = 330)

    #TEXT BOX
    t1=ttk.Entry(root,width=24,font = ("Comic Sans MS bold",24))
    t1.place(x = 800, y = 330,height=55)

    #FUNCTIONS
    def delete_button():
        book_code=t1.get().strip()
        

        if book_code=='':

            messagebox.showerror("ERROR","FIELD CANNOT BE EMPTY",parent=root)

            t1.delete(0,END)

        else:
            cur.execute('select status from books where book_code="{}"'.format(book_code))
            b=cur.fetchone()
            
            if b!=None and b[0]=='Issued':

                messagebox.showerror("ERROR","BOOK IS CURRENTLY ISSUED",parent=root)

                t1.delete(0,END)

            else:
                cur.execute('select book_code from books')
                flag2=False
                data=cur.fetchall()

                for i in data:
                    if i[0]==book_code:
                        flag2=True
                        break

                if flag2==False:
                    messagebox.showerror("ERROR","THIS BOOK CODE DOES NOT EXISTS",parent=root)
                    t1.delete(0,END)

                else:
                    cur.execute('delete from books where Book_Code="{}"'.format(book_code))
                    mycon.commit()
                    messagebox.showinfo("SUCCESS","BOOK DELETED SUCCESSFULY",parent=root)
                    t1.delete(0,END)

    #BUTTONS
    btn1=Button(root,text='DELETE',font = ("Comic Sans MS bold",25),padx=40,fg='#041926',pady=5,bg='#C1A7C8',borderwidth=3,relief='solid',command=delete_button)
    btn1.place(y=570,x=420)

    btn2=Button(root,text='GO BACK',font = ("Comic Sans MS bold",25),padx=40,pady=5,fg='#041926',borderwidth=3,bg='#C1A7C8',relief='solid',command=root.destroy)
    btn2.place(y=570,x=850)

    root.mainloop()
