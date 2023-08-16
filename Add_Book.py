from tkinter import *
import mysql.connector as con
from tkinter import ttk
from tkinter import messagebox

def book_add():
    mycon=con.connect(host='localhost',user='root',passwd='cricket2004',database='cs_project')
    cur=mycon.cursor()

    root=Toplevel()
    root.title('Add Books')
    root.state('zoomed')

    #BACKGROUND IMAGE
    bg = PhotoImage(file = "scenery.png")
    lbl1 = Label(root, image = bg,borderwidth=0)
    lbl1.place(x = 0,y = 0)

    #LABELS
    lb1=Label(root,text='ADD BOOKS',font = ("Comic Sans MS bold",37),padx=20,pady=10,borderwidth=3,relief='solid',bg='#63DA3C',fg='white')
    lb1.place(x=560,y=40)

    lb2=Label(root, bg='#63DA3C',fg='White',text = "ENTER BOOK NAME:", font = ("Comic Sans MS bold",20),padx=30,pady=5,width=24)
    lb2.place(x=200,y=260)

    lb3=Label(root, bg='#63DA3C',fg='White',text = "ENTER AUTHOR:", font = ("Comic Sans MS bold",20),padx=30,pady=5,width=24)
    lb3.place(x=200,y=340)

    lb4=Label(root, bg='#63DA3C',fg='White',text = "ENTER GENRE:", font = ("Comic Sans MS bold",20),padx=30,pady=5,width=24)
    lb4.place(x=200,y=420)

    #TEXT BOX
    t1=ttk.Entry(root,width=26,font = ("Comic Sans MS bold",20))
    t1.place(x=750,y=260,height=50)

    t2=ttk.Entry(root,width=26,font = ("Comic Sans MS bold",20))
    t2.place(x=750,y=340,height=50)

    t3=ttk.Combobox(root,height=10,values=['Genre','Novel','Biographies','Educational','Fiction','Romance','Horror','Poetry','Fantasy','Crime','History','Narrative','Mystery','Thriller','Suspense','Dystopian',"Children's",'Inspirational','Politics','Spirituality','Health'],font = ("Comic Sans MS bold",20),state='readonly')
    t3.current(0)
    t3.place(x=750,y=420,height=52,width=423)

    #FUNCTIONS
    def add_button():
        book_name=t1.get().strip()
        book_author=t2.get().strip()
        book_genre=t3.get() 

        if book_name=='' or book_author=='':
            messagebox.showerror("ERROR","NO FIELD CAN BE EMPTY",parent=root)
            t1.delete(0,END)
            t2.delete(0,END)
            t3.current(0)

        elif book_genre=='Genre':
            messagebox.showerror("ERROR","PLEASE SELECT A GENRE",parent=root)
            t1.delete(0,END)
            t2.delete(0,END)
            t3.current(0)

        else:
            cur.execute('select Name_of_Book,Author from books')
            l=cur.fetchall()
            flag=True

            if l!=None:
                for i in l:
                    if i[0]==book_name and i[1]==book_author:
                        flag=False

            if flag==False:
                messagebox.showerror("ERROR","THIS BOOK ALREADY EXISTS",parent=root)
                t1.delete(0,END)
                t2.delete(0,END)
                t3.current(0)

            else:
                cur.execute('select max(book_code) from books where genre="{}"'.format(book_genre))
                l=cur.fetchone()

                if l[0]!=None:
                    book_code=l[0]
                    digit=int(book_code[3:])
                    digit+=1

                    if digit>=100:
                        book_code=book_code[:3].upper()+str(digit)

                    elif  digit>=10:
                        book_code=book_code[:3]+'0'+str(digit)

                    else:
                        book_code=book_code[:3]+'00'+str(digit)

                else:
                    book_code=book_genre[:3].upper()+'001'

                cur.execute('insert into books(Name_of_Book, Author, Book_Code, Genre, Status) values ("{}","{}","{}","{}","{}")'.format(book_name,book_author,book_code,book_genre,'Not Issued'))
                mycon.commit()
                messagebox.showinfo("SUCCESS","BOOK ADDED SUCCESSFULY",parent=root)
                t1.delete(0,END)
                t2.delete(0,END)
                t3.current(0)

    #BUTTONS
    btn1=Button(root,text='ADD',font = ("Comic Sans MS bold",24),bg='#63DA3C',fg='white',width=10,borderwidth=3,relief='solid',command=add_button)
    btn1.place(x=390,y=580)

    btn2=Button(root,text='GO BACK',font = ("Comic Sans MS bold",24),width=10,bg='#63DA3C',fg='white',borderwidth=3,relief='solid',command=root.destroy)
    btn2.place(x=830,y=580)

    root.mainloop()
