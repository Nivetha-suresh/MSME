#PROGRAM TO CHECK THE ELIGIBILITY OF VOTE

from tkinter import *
from tkinter import messagebox
import os
a=Tk()
a.geometry("200x200")
def age_check():
    age_no=int(age.get())
    if age_no <= 18:
        messagebox.showerror("Invalid","should be greater than 18")
    else:
        print(age_no)
        messagebox.showinfo("information","eligible to vote")

def getin():
    n=name.get()
    ag=int(age.get())
    print(n)
    age_check()
b=Label(a,text="Vote eligibility")
b.pack()
b=Button(a,text="click",bg="green",command=getin)
b.pack()
name=Entry(a)
name.pack()
age=Entry(a)
age.pack()
a.mainloop()