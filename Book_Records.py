from tkinter import *
import mysql.connector as con
from tkinter import ttk

def book_records():

    mycon=con.connect(host='localhost',user='root',passwd='cricket2004',database='cs_project')
    cur=mycon.cursor()
    r1=Tk()   
    r1.title('ISSUED BOOK RECORDS')
    r1.state('zoomed')
    r1.geometry('1920x1080')

    main_frame = Frame(r1,borderwidth=0,bg='#9EE2FF')
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame,borderwidth=0,bg='#9EE2FF')
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_scrollbar1= ttk.Scrollbar(my_canvas, orient=HORIZONTAL, command=my_canvas.xview)
    my_scrollbar1.pack(side=BOTTOM, fill=X)

    my_canvas.configure(yscrollcommand=my_scrollbar.set, xscrollcommand=my_scrollbar1.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    second_frame = Frame(my_canvas,borderwidth=0,bg='#9EE2FF')   

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")

    #LABELS
    l1=Label(second_frame,text='NAME',borderwidth=3,relief='solid',font = ("Comic Sans MS bold",17),bg='purple',fg='white',pady=10,width=18)
    l1.grid(row=0,column=0,padx=30,pady=10)

    l2=Label(second_frame,text='ADMISSION NUMBER',borderwidth=3,relief='solid', font = ("Comic Sans MS bold",17),bg='purple',pady=10,padx=17,fg='white')
    l2.grid(row=0,column=1,padx=30,pady=10)

    l3=Label(second_frame,text='BOOK NAME',borderwidth=3,relief='solid', font = ("Comic Sans MS bold",17),bg='purple',pady=10,fg='white',width=25)
    l3.grid(row=0,column=2,padx=30,pady=10)

    l4=Label(second_frame,text='BOOK CODE',borderwidth=3,relief='solid',bg='purple', font = ("Comic Sans MS bold",17),pady=8,fg='white',width=16)
    l4.grid(row=0,column=3,padx=20,pady=10)

    l5=Label(second_frame,text='DATE OF ISSUE',borderwidth=3,relief='solid',bg='purple', font = ("Comic Sans MS bold",17),pady=10,fg='white',width=16)
    l5.grid(row=0,column=4,padx=20,pady=10)

    l6=Label(second_frame,text='DATE OF RETURN',borderwidth=3,relief='solid',bg='purple', font = ("Comic Sans MS bold",17),pady=10,fg='white',width=16)
    l6.grid(row=0,column=5,padx=20,pady=10)

    l7=Label(second_frame,text='DUE DATE',borderwidth=3,relief='solid',bg='purple', font = ("Comic Sans MS bold",17),pady=10,fg='white',width=16)
    l7.grid(row=0,column=6,padx=20,pady=10)

    l8=Label(second_frame,text='ISSUE TIME',borderwidth=3,relief='solid',bg='purple', font = ("Comic Sans MS bold",17),pady=10,fg='white',width=16)
    l8.grid(row=0,column=7,padx=20,pady=10)

    cur.execute('select * from book_records order by date_of_issue desc, issue_time desc')
    books=cur.fetchall()

    for i in range(len(books)):
        lb1=Label(second_frame,text=books[i][0],wraplength=240,borderwidth=3,relief='solid', font = ("Comic Sans MS bold",14),fg='white',bg='#54E346',padx=8,pady=5,width=20)
        lb1.grid(row=i+1,column=0,padx=10,pady=10)

        lb2=Label(second_frame,text=books[i][1],borderwidth=3,wraplength=160,relief='solid', font = ("Comic Sans MS bold",14),fg='white',bg='red',padx=5,pady=5,width=14)
        lb2.grid(row=i+1,column=1,padx=10,pady=10)

        lb3=Label(second_frame,text=books[i][2],borderwidth=3,wraplength=380,relief='solid', font = ("Comic Sans MS bold",14),fg='white',bg='#0123ff',padx=5,pady=5,width=32)
        lb3.grid(row=i+1,column=2,padx=30,pady=10)

        lb4=Label(second_frame,text=books[i][3],borderwidth=3,relief='solid', font = ("Comic Sans MS bold",14),fg='white',bg='#ff02ae',padx=5,pady=5,width=7)
        lb4.grid(row=i+1,column=3,padx=10,pady=10)

        issue_date=books[i][4].strftime('%d/%m/%Y')     

        lb5=Label(second_frame,text=issue_date,borderwidth=3,relief='solid', font = ("Comic Sans MS bold",14),fg='white',bg='#F98404',padx=5,pady=5,width=11)
        lb5.grid(row=i+1,column=4,padx=10,pady=10)

        if books[i][5]==None:
            lb6=Label(second_frame,text='-',borderwidth=3,relief='solid', font = ("Comic Sans MS bold",14),fg='white',bg='#54E346',padx=5,pady=5,width=11)
            lb6.grid(row=i+1,column=5,padx=10,pady=10)
        else:
            return_date=books[i][5].strftime('%d/%m/%Y')
            lb6=Label(second_frame,text=return_date,borderwidth=3,relief='solid', font = ("Comic Sans MS bold",14),fg='white',bg='#54E346',padx=5,pady=5,width=11)
            lb6.grid(row=i+1,column=5,padx=10,pady=10)

        due_date=books[i][6].strftime('%d/%m/%Y')

        lb7=Label(second_frame,text=due_date,borderwidth=3,relief='solid', font = ("Comic Sans MS bold",14),fg='white',bg='red',padx=5,pady=5,width=11)
        lb7.grid(row=i+1,column=6,padx=10,pady=10)

        lb8=Label(second_frame,text=books[i][7],borderwidth=3,relief='solid', font = ("Comic Sans MS bold",14),fg='white',bg='#0123ff',padx=5,pady=5,width=11)
        lb8.grid(row=i+1,column=7,padx=10,pady=10)

    r1.mainloop()
