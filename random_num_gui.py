import random
from tkinter import *
from tkinter import messagebox
a=random.randint(1,10)
c=Tk()
c.geometry("400x400")
def game():
    for i in range(1):
        b=int(e.get())
        if b<1 or b>10:
            break
        if a==b:
            print(a,"=",b)
            messagebox.showinfo("HOORY","YOU WON")
            break
        else:
            print("guess once again")
            messagebox.showinfo("NOT EQUAL","BETTER LUCK NEXT TIME")
d=Label(c,text="Guessing Game",bg="blue",fg="black")
d.pack()
e=Entry(c)
e.pack()
button=Button(c,text="click",bg="green",command=game)
button.pack()
c.mainloop()
