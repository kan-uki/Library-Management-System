from tkinter import *
from Details_Student import *
from Details_Staff import *
from Details_Book import *
from Book_Records import *

def admin():
    root1=Toplevel()
    root1.title('Admin')
    root1.geometry('1080x720+200+35')
    root1.state('zoomed')

    bg = PhotoImage(file = "snow.png")
    lbl1 = Label(root1, image = bg, borderwidth=0)
    lbl1.place(x = 0,y = 0) 

    #LABELS
    lbl = Label(root1, bg='#4cbb17',fg='White',text = "ADMIN", font = ("Comic Sans MS bold",40),pady=5,borderwidth=8,relief='ridge',width=15)
    lbl.place(x=530,y=40)

    #BUTTONS
    btn1 = Button(root1, text = "BOOK DETAILS", pady = 20,font=('Comic Sans MS',20),borderwidth=5,bg='#9ACD32',fg='white',command=book_details,width=25)
    btn1.place(x=570,y=180)

    btn2 = Button(root1, text = "VIEW BOOK RECORDS", pady = 20,font=('Comic Sans MS',20),borderwidth=5,bg='#9ACD32',fg='white',command=book_records,width=25)
    btn2.place(x=570,y=300)

    btn3 = Button(root1, text = "STUDENT DETAILS", pady = 20,font=('Comic Sans MS',20),borderwidth=5,bg='#9ACD32',fg='white',command=student_details,width=25)
    btn3.place(x=570,y=420)

    btn4 = Button(root1, text = "STAFF DETAILS", pady = 20,font=('Comic Sans MS',20),borderwidth=5,bg='#9ACD32',fg='white',command=staff_details,width=25)
    btn4.place(x=570,y=540)

    btn5=Button(root1,text='GO BACK', pady = 20,font=('Comic Sans MS',20),borderwidth=5,bg='#9ACD32',fg='white',command=root1.destroy,width=25)
    btn5.place(x=570,y=660)

    root1.mainloop()