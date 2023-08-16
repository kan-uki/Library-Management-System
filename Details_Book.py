from tkinter import *
from Add_Book import *
from Delete_Book import *
from View_Book import *

def book_details():
    root=Toplevel()
    root.title('Book Details')
    root.geometry('1080x720+200+35')
    root.state('zoomed')

    #BACKGROUND IMAGE
    bg = PhotoImage(file = "Sunrise.png")
    lbl1 = Label(root, image = bg,borderwidth=0)
    lbl1.place(x = 0,y = 0)

    #LABELS
    lbl = Label(root, bg='#FB9300',fg='White',text = "BOOK DETAILS", font = ("Comic Sans MS bold",35),padx=20,width=15,pady=5,borderwidth=10,relief='ridge')
    lbl.place(x=530,y=70)

    #BUTTONS
    btn1 = Button(root, text = "ADD BOOK DETAILS", pady = 20,font=('Comic Sans MS',20),borderwidth=5,bg='#9B72AA',fg='white',width=25,command=book_add)
    btn1.place(x=570,y=220)

    btn2 = Button(root, text = "DELETE BOOK DETAILS", pady = 20,font=('Comic Sans MS',20),borderwidth=5,bg='#9B72AA',fg='white',width=25,command=book_delete)
    btn2.place(x=570,y=350)

    btn3 = Button(root, text = "VIEW BOOK DETAILS", pady = 20,font=('Comic Sans MS',20),borderwidth=5,bg='#9B72AA',fg='white',width=25,command=book_list)
    btn3.place(x=570,y=480)

    btn4 = Button(root,text='GO BACK', pady = 20,font=('Comic Sans MS',20),borderwidth=5,bg='#9B72AA',fg='white',command=root.destroy,width=25)
    btn4.place(x=570,y=610)

    root.mainloop()