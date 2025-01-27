#SIMPLE TKINTER PROGRAMS
#PROGRAM 1

from tkinter import *
from tkinter import messagebox
import os
a=Tk()
a.geometry("200x200")
# def abc():
#     s=e.get()
#     print(s)
# b=Label(a,text="python",fg="red")
# b.pack()
# e=Entry(a)
# e.pack()
# c=Button(a,text="button",bg="green",command=abc)
# c.pack()
# a.mainloop()

#PROGRAM 2
# messagebox.showinfo("info","information")
# messagebox.showwarning("warning","alert")
# messagebox.showerror("error","invalid")
# messagebox.askyesno("questionary","are you ok")
# a.mainloop()

#PROGRAM 3
def shutdown():
    os.system("Shutdown /r /t 10")
b=Label(a,text="python",fg="red")
b.pack()
e=Entry(a)
e.pack()
c=Button(a,text="button",bg="green",command=shutdown())
c.pack()
a.mainloop()