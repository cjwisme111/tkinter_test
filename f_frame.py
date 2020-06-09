# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()

# f = Frame(root,width=200,height=100,bg="yellow", borderwidth=10, relief="flat").pack()  # 像素
f = Frame(root,width=100,height=100,bg="yellow", borderwidth=10, relief="raised").pack(side="top",anchor="w")  # 像素
f = Frame(root,width=100,height=100,bg="red",borderwidth=10, relief="sunken").pack(side="top",anchor="w")  # 像素
# f = Frame(root,width=200,height=100,bg="yellow", relief="flat").pack()  # 像素

root.mainloop()