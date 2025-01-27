from tkinter import *
from tkinter import messagebox

a=Tk()
a.geometry("200x200")
def inp():
    name=e.get()
    while name == '':
        messagebox.showerror("WARNING","ENTER NAME")
    for i in name:
        if i.isupper():
            print(''.join(i), end='')
    print('\n')
    for j in name:
        if j.islower():
            print(''.join(j), end='')
    print('\n')
    messagebox.showinfo("info","SUCCESSFULLY SPLITED")
l=Label(a,text="SAMPLE")
l.pack()
e=Entry(a)
e.pack()
b=Button(a,text="click",bg="blue",command=inp)
b.pack()
a.mainloop()
