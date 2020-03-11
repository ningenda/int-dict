from tkinter import *


window=Tk()

window.wm_title("Dictionary")

l1=Label(window,text="Enter Word")
l1.grid(row=0,column=0)



word_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)


list1=Listbox(window, height=6, width=35)
list1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>')



b2=Button(window,text="Search Entry",width=12,)
b2.grid(row=3,column=3)

window.mainloop()
