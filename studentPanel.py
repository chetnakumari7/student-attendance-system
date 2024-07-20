from tkinter import *
import sqlite3
from tkinter import messagebox, PhotoImage
from tkinter import ttk
from datetime import datetime

# from tkinter.ttk import *
# # from PIL import ImageTk, Image
# from tkinter import *
# import sqlite3
# from tkinter import messagebox
# from tkinter import ttk



class studentPanel:
    def __init__(self):
        
        global y 
        y  =Tk()
        y.geometry('600x600')
        y.config(bg='#57cc99')
        
        l0 = Label(y,text='Student Profile',font=("Helvetica", 25),bg='#57cc99',highlightthickness=0)
        l0.pack()
        
        l = Label(y,text='Name',bg='#57cc99',highlightthickness=0)
        l.pack()
        self.e = Entry(y)
        self.e.pack()
        
        l1 = Label(y,text='email',bg='#57cc99',highlightthickness=0)
        l1.pack()
        self.e1 = Entry(y)
        self.e1.pack()
        
        l2 = Label(y,text='password',bg='#57cc99',highlightthickness=0)
        l2.pack()
        self.e2 = Entry(y)
        self.e2.pack()

        l3 = Label(y,text='branch',bg='#57cc99',highlightthickness=0)
        l3.pack()
        self.e3 = Entry(y)
        self.e3.pack()

        l4 = Label(y,text='Roll No.',bg='#57cc99',highlightthickness=0)
        l4.pack()
        self.e4 = Entry(y)
        self.e4.pack()
        
        
        b = Button(y,text=' Registration ',bg='#57cc99', command= self.signup)
        b.place(x=200,y=300)
       
        
        b1 = Button(y,text='   Login   ',bg='#57cc99',command=self.login)
        b1.place(x=350,y=300)
        
        
        
    def signup(self):
        
       
        db = sqlite3.connect('attendance.db')
        cr = db.cursor()
        cr.execute(f''' insert into student_det values('{self.e.get()}', '{self.e1.get()}', '{self.e2.get()}', '{self.e3.get()}', '{self.e4.get()}')''')
        db.commit()
        messagebox.showinfo('Registration ','successfully')
        y.destroy()
        
    
    def login(self):
        y.destroy()
        global win1
        win1 = Tk()
        win1.geometry('300x300')
        win1.config(bg='#ded463')
        
        l1 = Label(win1,text= 'email',bg='#ded463',highlightthickness=0)
        l1.pack()
        self.e1 = Entry(win1)
        self.e1.pack()
        
        l2 = Label(win1,text= 'password',bg='#ded463',highlightthickness=0)
        l2.pack()
        self.e2 = Entry(win1)
        self.e2.pack()
        
        b = Button(win1,text='LOGIN', command=self.log1,bg='#ded463')
        b.pack()
        
     
        
    def log1(self):
        
        db = sqlite3.connect('attendance.db')
        cr = db.cursor()
        cr.execute(f''' select * from student_det where email = '{self.e1.get()}' and password = '{self.e2.get()}' ''')
        data = cr.fetchall()
        print(data)
        if (len(data) != 0):
            win1.destroy()
            
            window2 = Tk() 
            window2.geometry('600x600')
         
            notebook = ttk.Notebook(window2)
            fr = Frame(window2,bg='#77d795')
            l = Label(fr, text="Welcome:  " + data[0][0].upper(), background='#77d795',highlightthickness=0,font=("Helvetica",25))
            l.place(x=200,y=20)
            l1 = Label(fr, text="EMAIL:  " + data[0][1], background='#77d795',highlightthickness=0)
            l1.place(x=20,y=100)
            l2 = Label(fr, text="PASSWORD:  " + data[0][2], background='#77d795',highlightthickness=0)
            l2.place(x=20,y=150)
            l3 = Label(fr, text="BRANCH:  " + data[0][3], background='#77d795',highlightthickness=0)
            l3.place(x=20,y=200)
            l3 = Label(fr, text="Roll no. :  " + str(data[0][4]), background='#77d795',highlightthickness=0)
            l3.place(x=20,y=250)
          
            
            fr.pack()
            notebook.pack(expand=True, fill='both')
            notebook.add(fr,text='Student profile')
            
            fr2 = Frame(window2,bg='#ced4da')
            l2 = Label(fr2,text='Attendance')
            l2.pack()
            
            tree  = ttk.Treeview(fr2, columns=('Name','Rollno','Attendance'))
            tree.heading('Name', text='Name')
            tree.heading('Rollno', text='Rollno')
            tree.heading('Attendance',text='Attendance')

            
            cr.execute(f" select *  from student_attendance where rollno = {data[0][4]} ")
            student = cr.fetchall()
            print(student)
            
            for i in range(0, len(student)):
                tree.insert("", 'end', values=(student[i][3], student[i][1], student[i][0]))
            
            tree.pack()
            
            fr2.pack()
            notebook.add(fr2,text='Attendance')
            
        else:
            messagebox.showwarning('Error','Incorrect email or password')


    
        
        


class TeacherPanel:
    def __init__(self):
        global win1
        win1 = Tk()
        win1.geometry('800x500')
        
        win1.config(bg='#61a5c2')
       
        l = Label(win1,text= 'Teacher Login',bg='#61a5c2',highlightthickness=0,font=("Helvetica", 20),)
        l.place(x=310,y=50)
        
        
        l1 = Label(win1,text= 'Email',bg='#61a5c2',highlightthickness=0)
        l1.place(x=300, y = 150 )
        self.e1 = Entry(win1)
        self.e1.place(x=400, y=150)
        
        l2 = Label(win1,text= 'Password',bg='#61a5c2',highlightthickness=0)
        l2.place(x = 300, y =200)
        self.e2 = Entry(win1,show='*')
        self.e2.place(x=400, y=200)
        
        b = Button(win1,text=' Login',  command= self.login, bg='#61a5c2')
        b.place(x=370,y=250)
       
    def data_updated(self):
        db = sqlite3.connect('attendance.db')
        cr = db.cursor()
        cr.execute(f''' update student_det set name = '{self.e.get()}' where email = '{self.e1.get()}' ''')
        db.commit()
        print('updated')
           
            

            
    def check(self): 
                print(self.v.get())
                                
    def login(self):
        db = sqlite3.connect('attendance.db')
        cr = db.cursor()
        cr.execute(f''' select * from teacher_det where email = '{self.e1.get()}' and password = '{self.e2.get()}' ''')
        self.data = cr.fetchone()
        
           
                
               
        
        if self.data:
            win1.destroy()
               
            
            self.tf = Tk()
            self.tf.geometry('800x500')
            self.tf.config(bg='#ff9770')
            
            
            l = Label(self.tf,text='WELCOME:  ' + self.data[0].upper(),font=("Helvetica",25),bg='#ff9770',highlightthickness=0)
            l.pack()
            
            notebook = ttk.Notebook(self.tf)
            fr = Frame(self.tf, bg= '#ff9770', padx=100, pady=50)
            l0 = Label(fr,font=("Helvetica", 20), text='Total Student',bg='#ff9770',highlightthickness=0, )
            l0.pack()
            
            tree  = ttk.Treeview(fr, columns=('Name','Rollno','Branch'))
            tree.heading('Name', text='Name')
            tree.heading('Rollno', text='Rollno')
            tree.heading('Branch', text='Branch')

            
            cr.execute(f" select *  from student_det where branch = '{self.data[2]}' ")
            self.student = cr.fetchall()
            print(self.student)
            
            for i in range(0, len(self.student)):
                tree.insert("", 'end', values=(self.student[i][0], self.student[i][4],self.student[i][3]))
            
            tree.pack()
            fr.pack()
            notebook.pack()
            notebook.add(fr, text='Students')
            # lb = Listbox(self.tf)
            # lb.pack()
            # for i in range(0,len(student)):
            #     lb.insert(i,student[i][0])
            
            
            fr2 = Frame(self.tf, bg='#ff9770')
            l0 = Label(fr2,font=("Helvetica", 15), text='Update Student Profile',bg='#ff9770',highlightthickness=0, )
            l0.pack()
            
            l = Label(fr2, text='name',bg='#ff9770',highlightthickness=0)
            l.pack()
            self.e = Entry(fr2)
            self.e.insert(0,self.student[0][0])
            self.e.pack()
            l1 = Label(fr2, text='email',bg='#ff9770',highlightthickness=0)
            l1.pack()
            
            self.e1 = Entry(fr2)
            self.e1.insert(0,self.student[0][1])
            self.e1.config(state='disabled')
            self.e1.pack()
            
            l2 = Label(fr2, text='password',bg='#ff9770',highlightthickness=0)
            l2.pack()
            
            self.e2 = Entry(fr2)
            self.e2.insert(0,self.student[0][2])
            
            self.e2.pack()
             
            b = Button(fr2, text='update', command=self.data_updated,bg='#ff9770')
            b.pack()
            
            fr2.pack()
            
            notebook.add(fr2, text='Profile')
            
            fr3 = Frame(self.tf, bg='hotpink')
            l31 = Label(fr3,font=("Helvetica", 20), text='Mark Attendance',bg='hotpink',highlightthickness=0, )
            l31.place(x=300, y=10)
            # l31.pack()
            
            
            self.date = datetime.now().date()
            db = sqlite3.connect('attendance.db')
            cr = db.cursor()
            cr.execute(f''' select * from student_det where branch = '{self.data[2]}' ''')
            data = cr.fetchall()
            self.v=IntVar()
            self.f=Checkbutton(fr3,onvalue=1,offvalue=0,variable=self.v,text="mamam")            
            self.f.grid(row=4,column=3)   

            self.d =[]
            self.c = []
            self.l = []
            self.l1=[]
            self.e=IntVar()
            

            for i in range(len(data)):
                self.l.append(Label(fr3,text=data[i][0]))
                self.l[i].grid(row = i, column = 0)
                self.l1.append(Label(fr3,text=data[i][4]))
                self.l[i].grid(row = i, column = 1)
                self.d.append(IntVar())
                self.c.append(Checkbutton(fr3, onvalue=1, offvalue=0,variable=self.d[i], text='Present'))
                self.c[i].grid(row=i, column = 2)
                
            b = Button(fr3,text='mark attendance', command=self.check)
            b.grid(row=len(data), column=1)
            
                              
                
            
            fr3.pack()
            notebook.add(fr3,text='Attendance')
            notebook.pack(expand=True, fill='both')
            
        
        else:            
            messagebox.showinfo('failure', 'wrong data')
      

            
            
           
            
            
        
