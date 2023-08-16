from tkinter import *
import mysql.connector as con
from tkinter import ttk, messagebox

def staff_add(): 
        mycon=con.connect(host='localhost',user='root',passwd='cricket2004',database='cs_project')

        cur=mycon.cursor()        
        
        r1=Toplevel()
                    
        r1.title('Add Staff Details')

        r1.state('zoomed')

        #BACKGROUND IMAGE
    
        bg = PhotoImage(file = "denmark.png")

        lbl1 = Label(r1, image = bg,borderwidth=0)

        lbl1.place(x = 0,y = 0)
                        
        #LABELS
                            
        lb1=Label(r1,text='ADD STAFF DETAILS',font = ("Comic Sans MS bold",40),padx=20,pady=10,borderwidth=3,relief='solid', bg='#008000',fg='White')
        
        lb1.place(x=450,y=50)

        lb2=Label(r1, bg='#9ACD32',fg='White',text = "ENTER NAME:", font = ("Comic Sans MS bold",20),padx=20,pady=5,width=24)
        
        lb2.place(x=270,y=250)

        lb4=Label(r1, bg='#9ACD32',fg='White',text = "ENTER GENDER:", font = ("Comic Sans MS bold",20),padx=20,pady=5,width=24)
                        
        lb4.place(x=270,y=325)

        lb5=Label(r1, bg='#9ACD32',fg='White',text = "ENTER ADDRESS:", font = ("Comic Sans MS bold",20),padx=20,pady=5,width=24)
                        
        lb5.place(x=270,y=400)

        lb6=Label(r1, bg='#9ACD32',fg='White',text = "ENTER PHONE NUMBER:", font = ("Comic Sans MS bold",20),padx=20,pady=5,width=24)
                        
        lb6.place(x=270,y=475)

        #TEXT BOXES

        t1=ttk.Entry(r1,width=26,font = ("Comic Sans MS bold",20))
        
        t1.place(x=780,y=250,height=50)

        dropdown=ttk.Combobox(r1,values=['Gender','M','F'],font = ("Comic Sans MS bold",22),state='readonly')

        dropdown.current(0)

        dropdown.place(x=780,y=325,width=422,height=52)

        t4=ttk.Entry(r1,width=26,font = ("Comic Sans MS bold",20))
        
        t4.place(x=780,y=400,height=50)

        t5=ttk.Entry(r1,width=26,font = ("Comic Sans MS bold",20))
        
        t5.place(x=780,y=475,height=50)

        def clear_fields():

                t1.delete(0,END)

                dropdown.current(0)

                t4.delete(0,END)

                t5.delete(0,END)

        def add_button():

                staff_name=t1.get().strip()
 
                gender=dropdown.get()
 
                address=t4.get().strip()
 
                ph_no=t5.get().strip()

                if staff_name=='' or address=='' or ph_no=='':
                
                    messagebox.showerror("ERROR",'NO FIELD CAN BE EMPTY',parent=r1)

                else:

                    if ph_no.isdigit()==False:

                        messagebox.showerror("ERROR",'PHONE NUMBER CAN ONLY BE DIGITS',parent=r1)

                        t5.delete(0,END)
                    
                    elif len(ph_no)!=10:

                        messagebox.showerror("ERROR",'PHONE NUMBER CAN ONLY BE 10 DIGITS LONG',parent=r1)

                        t5.delete(0,END)

                    elif gender=='Gender':

                        messagebox.showerror("ERROR",'PLEASE SELECT A GENDER',parent=r1)

                    else: 
                        flag=True

                        cur.execute('select phone_number from staff')
                        
                        l=cur.fetchall()

                        if l!=None:
                        
                            for i in l:
                        
                                if i[0]==ph_no:
                        
                                    flag=False

                        if flag==False:

                            messagebox.showerror("ERROR",'STAFF WITH SAME PHONE NUMBER EXISTS',parent=r1)

                            t1.delete(0,END)
                        
                            dropdown.current(0)
                        
                            t4.delete(0,END)
                        
                            t5.delete(0,END)

                        else:
                            cur.execute('select max(staffid) from staff')
                        
                            l=cur.fetchone()

                            if l[0]!=None:

                                staff_id=(l[0] + 1)

                            else:
                                
                                staff_id=1

                            cur.execute('insert into staff values("{}",{},"{}","{}","{}")'.format(staff_name,staff_id,gender,address,ph_no))
                        
                            mycon.commit()

                            messagebox.showinfo("SUCCESS",'RECORD SUCCESSFULLY ADDED',parent=r1)

                            t1.delete(0,END)
                        
                            dropdown.current(0)
                        
                            t4.delete(0,END)
                        
                            t5.delete(0,END)

        btn1 = Button(r1, text = "ADD STAFF DETAILS", padx = 20, pady = 20,font=('Comic Sans MS',15),borderwidth=3,relief='solid',bg='#008000',fg='white',width=17,command=add_button)

        btn1.place(x=269,y=630)  

        btn2 = Button(r1, text = "CLEAR", padx = 20, pady = 20,font=('Comic Sans MS',15),borderwidth=3,relief='solid',bg='#008000',fg='white',width=15,command=clear_fields)

        btn2.place(x=625,y=630)              
        
        btn3 = Button(r1, text = "GO BACK", padx = 25, pady = 20,font=('Comic Sans MS',15),borderwidth=3,relief='solid',bg='#008000',fg='white',width=15,command=r1.destroy)

        btn3.place(x=960,y=630)

        r1.mainloop()
