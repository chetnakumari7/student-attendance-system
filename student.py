from tkinter import *
import sqlite3
from tkinter import ttk
from studentPanel import studentPanel,TeacherPanel

win = Tk()
win.geometry('800x500')

win.title('Laapta University') 

note = ttk.Notebook()






frame = Frame(win, bg='#3a698d', padx=170, pady=50,)


l = Label(frame,text='Laapta University',image='',  font=("Helvetica", 25), bg ='#3a698d', highlightthickness=0, )
l.pack()

l2 = Label(frame,text='Laapta University is a prestigious institution \nrenowned for its dedication to\n academic excellence and innovative', font=("Helvetica", 15), bg ='#3a698d', highlightthickness=0)
l2.pack()

b = Button(frame, command=studentPanel, text='Student', foreground='blue')
b.place(x=280,y= 200)
b1 = Button(frame, command=TeacherPanel, text='Teacher', foreground='blue')
b1.place(x=80, y = 200)
frame.pack()

frame2 = Frame(win,bg='blue')

frame2.pack()
#code

frame3 = Frame(win,bg='green')
#code
frame3.pack()


note.add(frame, text='University')
note.add(frame2,text='Services')
note.add(frame3,text='Contact-US')

note.pack(expand=True, fill='both')


mainloop()


