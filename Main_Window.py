from tkinter import *
from Student import *
from Password_Admin import *

window = Tk()
window.title("Library Management System")
window.state('zoomed')
window.geometry("1080x720+200+35")

#BACKGROUND IMAGE
bg = PhotoImage(file = "1.png")
img = Label(window, image = bg,borderwidth=0)
img.place(x = 0,y = 0)

#LABELS
lb1 = Label(window, bg='#FFEBCD',fg='#7c5b07',text = "WELCOME TO TTM LIBRARY", font = ("Comic Sans MS bold",34),padx=5,pady=5,borderwidth=10,relief='ridge')
lb1.pack(pady = 80)

from tkinter.font import Font
font = Font(family = "Comic Sans MS", size = 14)
window.option_add("*TCombobox*Listbox*Font", font)

#BUTTONS
btn1 = Button(window, text = "STUDENT", padx = 75, pady = 20,font=('Comic Sans MS',22),borderwidth=5,bg='#DEB887',fg='#7c5b07',command=student)
btn1.pack(pady=10)

btn2 = Button(window, text = "ADMIN", padx = 92, pady = 20,font=('Comic Sans MS',22),borderwidth=5,bg='#DEB887',fg='#7c5b07',command=password)
btn2.pack(pady=10)

btn3 = Button(window, text = "EXIT", padx = 107, pady = 20,font=('Comic Sans MS',22),borderwidth=5,bg='#DEB887',fg='#7c5b07',command=window.destroy)
btn3.pack(pady=10)
window.mainloop()