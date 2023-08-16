from tkinter import *
from Add_Student import *
from View_Student import *
from Delete_Student import *

def student_details():
    t1 = Toplevel()
    t1.title("Student Details")
    t1.geometry('1080x720+200+35')
    t1.state('zoomed')

    bg = PhotoImage(file = "chakri.png")
    lbl1 = Label(t1, image = bg,borderwidth=0)
    lbl1.place(x = 0,y = 0)

    #LABELS
    lbl = Label(t1, bg='orange',fg='White',text = "STUDENT DETAILS", font = ("Comic Sans MS bold",35),padx=20,pady=5,borderwidth=10,relief='ridge')
    lbl.pack(pady = 45)

    #BUTTONS
    btn1 = Button(t1, text = "ADD STUDENT DETAILS", pady = 20,font=('Comic Sans MS',20),borderwidth=5,bg='#00bfff',fg='white',width=30, command = student_add)
    btn1.pack(pady=13)

    btn2 = Button(t1, text = "DELETE STUDENT DETAILS", pady = 20,font=('Comic Sans MS',20),borderwidth=5,bg='#00bfff',fg='white', width=30, command = student_delete)
    btn2.pack(pady=13)

    btn3 = Button(t1, text = "VIEW STUDENT DETAILS", pady = 20,font=('Comic Sans MS',20),borderwidth=5,bg='#00bfff',fg='white',width=30, command = student_view)
    btn3.pack(pady=13)

    btn4=Button(t1,text='GO BACK', pady = 20,font=('Comic Sans MS',20),borderwidth=5,bg='#00bfff',fg='white',command=t1.destroy,width=30)
    btn4.pack(pady=13)

    t1.mainloop()