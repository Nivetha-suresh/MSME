from tkinter import *
from tkinter import messagebox
import os
a=Tk()
a.geometry("400x500")

def discount_calci():
    s=int(amount.get())
    if s<=1000:
        messagebox.showinfo("discount","No discount")
        print("Amount to pay is",s)
    elif(s>1000 and s<5000):
        messagebox.showinfo("discount","20 percent")
        print(f'Amount to pay is {s-(s*(20/100))}')
    else:
        messagebox.showinfo("discount","10 percent")

l=Label(a,text="DISCOUNT CALCULATOR",fg="red")
l.grid(row=1,column=1)

l1=Label(a,text="Amount",bg="grey")
l1.grid(row=2,column=1)

amount=Entry(a)
amount.grid(row=2,column=2)

b=Button(a,text="check",command=discount_calci)
b.grid(row=3,column=3)

a.mainloop()