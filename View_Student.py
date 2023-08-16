from tkinter import *
from tkinter import ttk
import mysql.connector as con

def student_view():
    mycon=con.connect(host='localhost',user='root',passwd='cricket2004',database='cs_project')
    cur=mycon.cursor()

    r1 = Toplevel()
    r1.title("View Student Details")
    r1.geometry('1080x720+200+35')
    r1.state('zoomed')

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
    l1=Label(second_frame,text='NAME',borderwidth=3,relief='solid',font = ("Comic Sans MS bold",20),bg='#d68438',fg='white',padx=100,pady=15)
    l1.grid(row=0,column=0,padx=13,pady=10)

    l2=Label(second_frame,text='DATE OF BIRTH',borderwidth=3,relief='solid', font = ("Comic Sans MS bold",20),bg='#f1b24b',padx=70,pady=15,fg='white')
    l2.grid(row=0,column=1,padx=13,pady=10)

    l3=Label(second_frame,text='ADMISSION NO.',borderwidth=3,relief='solid', font = ("Comic Sans MS bold",20),bg='#36846b',padx=30,pady=15,fg='white')
    l3.grid(row=0,column=2,padx=13,pady=10)

    l4=Label(second_frame,text='CLASS',borderwidth=3,relief='solid',bg='#4bb39a', font = ("Comic Sans MS bold",20),padx=40,pady=15,fg='white')
    l4.grid(row=0,column=3,padx=13,pady=10)

    l5=Label(second_frame,text='SECTION',borderwidth=3,relief='solid',bg='#d68438', font = ("Comic Sans MS bold",20),padx=40,pady=15,fg='white')
    l5.grid(row=0,column=4,padx=13,pady=10)

    cur.execute('select * from student')
    student=cur.fetchall()

    for i in range(len(student)):
        for j in range(len(student[i])):

            if j == 0:
                label = Label(second_frame,text=student[i][j],wraplength=240,borderwidth=3,relief='solid', font = ("Comic Sans MS bold",15),bg='#d68438',padx=5,pady=5,width=20)
                label.grid(row=i+1,column=j,padx=10,pady=10)

            elif j == 1:
                label = Label(second_frame,text=student[i][j],borderwidth=3,relief='solid', font = ("Comic Sans MS bold",15),bg='#f1b24b',padx=5,pady=5,width=15)
                label.grid(row=i+1,column=j,padx=10,pady=10)

            elif j == 2:
                label = Label(second_frame,text=student[i][j],wraplength=180,borderwidth=3,relief='solid', font = ("Comic Sans MS bold",15),bg='#36846b',padx=5,pady=5,width=15)
                label.grid(row=i+1,column=j,padx=10,pady=10)

            elif j == 3:
                label = Label(second_frame,text=student[i][j],borderwidth=3,relief='solid', font = ("Comic Sans MS bold",15),bg='#4bb39a',padx=5,pady=5,width=5)
                label.grid(row=i+1,column=j,padx=10,pady=10)

            elif j == 4:
                label = Label(second_frame,text=student[i][j],borderwidth=3,relief='solid', font = ("Comic Sans MS bold",15),bg='#d68438',padx=5,pady=5,width=5)
                label.grid(row=i+1,column=j,padx=10,pady=10)

    r1.mainloop()
