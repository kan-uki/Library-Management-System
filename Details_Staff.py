from tkinter import *
from Add_Staff import *
from Delete_Staff import *
from View_Staff import * 

def staff_details():
        r1=Toplevel()
        r1.state('zoomed')
        r1.title('Staff Details')

        #BACKGROUND IMAGE
        bg = PhotoImage(file = "Waterfall.png")
        lbl1 = Label(r1, image = bg,borderwidth=0)
        lbl1.place(x = 0,y = 0)

        #LABELS
        lbl = Label(r1, bg='#FB9300',fg='White',text = "STAFF DETAILS", font = ("Comic Sans MS bold",35),padx=20,width=16,pady=5,borderwidth=10,relief='ridge')
        lbl.place(x=533,y=70)

        #BUTTONS
        btn1 = Button(r1, text = "ADD STAFF DETAILS", padx = 20, pady = 20,font=('Comic Sans MS',20),borderwidth=5,bg='#81B214',fg='white',width=25,command=staff_add)
        btn1.place(x=570,y=220)

        btn2 = Button(r1, text = "DELETE STAFF DETAILS", padx = 20, pady = 20,font=('Comic Sans MS',20),borderwidth=5,bg='#81B214',fg='white',width=25,command=staff_delete)
        btn2.place(x=570,y=350)

        btn3 = Button(r1, text = "VIEW STAFF DETAILS", padx = 20, pady = 20,font=('Comic Sans MS',20),borderwidth=5,bg='#81B214',fg='white',width=25,command=staff_view)
        btn3.place(x=570,y=480)

        btn4 = Button(r1, text = "GO BACK", padx = 20, pady = 20,font=('Comic Sans MS',20),borderwidth=5,bg='#81B214',fg='white',width=25,command=r1.destroy)
        btn4.place(x=570,y=610)        

        r1.mainloop()