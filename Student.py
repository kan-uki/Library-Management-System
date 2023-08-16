from tkinter import *
from Issue import *
from Booklist import *
from Return import *

def student():
    root=Toplevel()
    root.title('Student')
    root.geometry('1920x1080')
    root.state('zoomed')

    #BACKGROUND IMAGE
    bg = PhotoImage(file = "snow.png")
    lbl1 = Label(root, image = bg,borderwidth=0)
    lbl1.place(x = 0,y = 0)

    #LABELS
    lbl = Label(root, bg='#4cbb17',fg='White',text = "STUDENT", font = ("Comic Sans MS bold",35),padx=20,pady=5,borderwidth=10,relief='ridge')
    lbl.pack(pady = 40)

    #BUTTONS
    btn1 = Button(root, text = "ISSUE BOOK", padx = 80, pady = 20,font=('Comic Sans MS',20),borderwidth=5,bg='#9ACD32',fg='white',command=issue)
    btn1.pack(pady=10)

    btn2 = Button(root, text = "RETURN BOOK", padx = 68, pady = 20,font=('Comic Sans MS',20),borderwidth=5,bg='#9ACD32',fg='white',command=return_book)
    btn2.pack(pady=10)

    btn3 = Button(root, text = "VIEW BOOK LIST", padx = 48, pady = 20,font=('Comic Sans MS',20),borderwidth=5,bg='#9ACD32',fg='white',command=book_list)
    btn3.pack(pady=10)

    btn4 = Button(root,text='GO BACK', padx = 109, pady = 20,font=('Comic Sans MS',20),borderwidth=5,bg='#9ACD32',fg='white',command=root.destroy)
    btn4.pack(pady=10)

    root.mainloop()