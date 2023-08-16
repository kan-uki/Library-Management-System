from tkinter import *
from tkinter import ttk,messagebox
from Admin import *
import mysql.connector as con

def password():

    mycon=con.connect(host='localhost',user='root',passwd='cricket2004',database='cs_project')
    cur=mycon.cursor()

    r1=Toplevel()
    r1.title('LOGIN')
    r1.geometry('960x340+300+170')
    r1.focus()

    #Background Image
    global bg
    bg = PhotoImage(file = "login.png")
    lbl1 = Label(r1, image = bg, borderwidth=0)
    lbl1.place(x = 0,y = 0) 

    #Labels
    lb1=Label(r1, bg='#32E875',fg='White',text = "ENTER USERNAME:", font = ("Comic Sans MS bold",20),padx=20,pady=1,width=20)
    lb1.place(x = 40, y = 30)

    lb2=Label(r1, bg='#32E875',fg='White',text = "ENTER PASSWORD:", font = ("Comic Sans MS bold",20),padx=20,pady=1,width=20)
    lb2.place(x = 40, y = 130)

    #Textbox
    t1=ttk.Entry(r1,width=24,font = ("Comic Sans MS bold",20))
    t1.place(x = 520, y = 30)

    t2=ttk.Entry(r1,width=24,font = ("Comic Sans MS bold",20),show='*')
    t2.place(x = 520, y = 130)

    #Login Function
    def login():
        name=t1.get()
        password=t2.get()

        cur.execute('select * from password')
        l = cur.fetchall()

        for i in l:
            if i[0]==name and i[1]==password:
                r1.destroy()
                admin()
                break
        else:
            messagebox.showerror("ERROR","EITHER THE USERNAME OR THE PASSWORD IS WRONG",parent=r1)
            t1.delete(0,END)
            t2.delete(0,END)

    def ch_password():
        r5=Toplevel()
        r5.title('CHANGE PASSWORD')
        r5.geometry('960x340+300+170')
        r5.focus()

        #Background Image
        img = Label(r5, image = bg, borderwidth=0)
        img.place(x = 0,y = 0)

        #Labels
        lb1=Label(r5, bg='#32E875',fg='White',text = "ENTER USERNAME:", font = ("Comic Sans MS bold",20),padx=20,pady=1,width=20)
        lb1.place(x = 40, y =15)

        lb2=Label(r5, bg='#32E875',fg='White',text = "ENTER OLD PASSWORD:", font = ("Comic Sans MS bold",20),padx=20,pady=1,width=20)
        lb2.place(x = 40, y = 85)

        lb3=Label(r5, bg='#32E875',fg='White',text = "ENTER NEW PASSWORD:", font = ("Comic Sans MS bold",20),padx=20,pady=1,width=20)
        lb3.place(x = 40, y = 155)

        #Textbox
        t1=ttk.Entry(r5,width=24,font = ("Comic Sans MS bold",20))
        t1.place(x = 520, y = 15)

        t2=ttk.Entry(r5,width=24,font = ("Comic Sans MS bold",20),show='*')
        t2.place(x = 520, y = 85)

        t3=ttk.Entry(r5,width=24,font = ("Comic Sans MS bold",20),show='*')
        t3.place(x = 520, y = 155)

        def change_password():
            name=t1.get()
            old_password=t2.get()
            new_password=t3.get()

            cur.execute('select * from password')
            l = cur.fetchall()

            for i in l:
                if i[0] == name and i[1]==old_password:
                    cur.execute('update password set password = "{}" where user_name = "{}"'.format(new_password, name))
                    mycon.commit()
                    messagebox.showinfo("SUCCESSFUL","PASSWORD HAS BEEN UPDATED SUCCESSFULLY",parent=r5)
                    r5.destroy()
                    break

            else:
                messagebox.showerror("ERROR","EITHER THE USERNAME OR THE OLD PASSWORD IS WRONG",parent=r5)
                t1.delete(0,END)
                t2.delete(0,END)
                t3.delete(0,END)

        btn1=Button(r5,text='CHANGE',font = ("Comic Sans MS bold",19),padx=20,pady=5,borderwidth=3,bg='#50CB93',fg='white',relief='solid', command = change_password)
        btn1.place(x = 220, y = 235)

        btn2=Button(r5,text='CANCEL',font = ("Comic Sans MS bold",19),padx=20,pady=5,borderwidth=3,bg='#50CB93',fg='white',relief='solid', command = r5.destroy)
        btn2.place(x = 550, y = 235)

    #Buttons
    btn1=Button(r1,text='CHANGE PASSWORD',font = ("Comic Sans MS bold",19),bg='#50CB93',fg='white',padx=20,pady=5,borderwidth=3,relief='solid', command = ch_password)
    btn1.place(x = 70, y = 220)

    btn2=Button(r1,text='LOGIN',font = ("Comic Sans MS bold",19),bg='#50CB93',fg='white',padx=20,pady=5,borderwidth=3,relief='solid', command = login)
    btn2.place(x = 520, y = 220)

    btn3=Button(r1,text='GO BACK',font = ("Comic Sans MS bold",19),bg='#50CB93',fg='white',padx=19,pady=5,borderwidth=3,relief='solid', command = r1.destroy)
    btn3.place(x = 750, y = 220)

    r1.mainloop()
