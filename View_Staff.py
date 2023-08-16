from tkinter import *
import mysql.connector as con
from tkinter import ttk

def staff_view():
    mycon=con.connect(host='localhost',user='root',passwd='cricket2004',database='cs_project')
    cur=mycon.cursor()

    r1=Toplevel()
    r1.state('zoomed')
    r1.title('View Staff Details')

    # Create A Main Frame
    main_frame = Frame(r1,borderwidth=0,bg='#9EE2FF')
    main_frame.pack(fill=BOTH, expand=1)

    # Create A Canvas
    my_canvas = Canvas(main_frame,borderwidth=0,bg='#9EE2FF')
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add A Scrollbar To The Canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    # Create ANOTHER Frame INSIDE the Canvas
    second_frame = Frame(my_canvas,borderwidth=0,bg='#9EE2FF')

    # Add that New frame To a Window In The Canvas
    my_canvas.create_window((0,0), window=second_frame, anchor="nw")

    #LABELS
    l1=Label(second_frame,text='NAME',borderwidth=3,relief='solid',font = ("Comic Sans MS bold",19),bg='purple',fg='white',width=17,pady=15)
    l1.grid(row=0,column=0,padx=22,pady=15)

    l2=Label(second_frame,text='STAFF ID',borderwidth=3,relief='solid', font = ("Comic Sans MS bold",19),bg='purple',width=11,pady=15,fg='white')
    l2.grid(row=0,column=1,padx=27,pady=15)

    l3=Label(second_frame,text='GENDER',borderwidth=3,relief='solid', font = ("Comic Sans MS bold",19),bg='purple',width=8,pady=15,fg='white')
    l3.grid(row=0,column=2,padx=27,pady=15)

    l4=Label(second_frame,text='ADDRESS',borderwidth=3,relief='solid',bg='purple', font = ("Comic Sans MS bold",19),padx=22,width=20,pady=15,fg='white')
    l4.grid(row=0,column=3,padx=22,pady=15)

    l5=Label(second_frame,text='CONTACT NUMBER',borderwidth=3,relief='solid',bg='purple', font = ("Comic Sans MS bold",19),padx=30,pady=15,fg='white')
    l5.grid(row=0,column=4,padx=22,pady=15)

    cur.execute('select * from staff')
    staff=cur.fetchall()

    for i in range(len(staff)):
        for j in range(len(staff[i])):

            if j==0:
                l=Label(second_frame,text=staff[i][j],borderwidth=3,wraplength=240,relief='solid',font = ("Comic Sans MS bold",15),bg='#DC143C',fg='white',width=21,pady=15)
                l.grid(row=i+1,column=j,padx=25,pady=10)
            elif j==1:
                l=Label(second_frame,text=staff[i][j],borderwidth=3,relief='solid',font = ("Comic Sans MS bold",15),bg='#00BFFF',fg='white',width=10,padx=5,pady=15)
                l.grid(row=i+1,column=j,padx=35,pady=10)
            elif j==2:
                l=Label(second_frame,text=staff[i][j],borderwidth=3,relief='solid',font = ("Comic Sans MS bold",15),bg='#FF1493',fg='white',width=5,padx=5,pady=15)
                l.grid(row=i+1,column=j,padx=35,pady=10)
            elif j==3:
                l=Label(second_frame,text=staff[i][j],borderwidth=3,wraplength=330,relief='solid',font = ("Comic Sans MS bold",15),bg='#40E0D0',fg='white',width=28,padx=5,pady=15)
                l.grid(row=i+1,column=j,padx=35,pady=10)
            else:
                l=Label(second_frame,text=staff[i][j],borderwidth=3,relief='solid',font = ("Comic Sans MS bold",15),bg='#008000',fg='white',width=15,padx=5,pady=15)
                l.grid(row=i+1,column=j,padx=35,pady=10)

    r1.mainloop()
