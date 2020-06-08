# -*- coding: utf-8 -*-

import tkinter as tk


windows = tk.Tk()
windows.title("list box widget")
windows.geometry("200x200")

var1 = tk.StringVar()
l = tk.Label(windows, textvariable=var1, height=2,width=10, bg="yellow")
l.pack()

def print_select_value():
    var1.set(listbox.get(listbox.curselection()))

b = tk.Button(windows, text="select menu", height=2, width=6,bg="green", command=print_select_value)
b.pack()
# 声明初始值
init_val = tk.StringVar()
# 添加初始值
init_val.set((11,22,33,44))
# 声明listbox
listbox = tk.Listbox(windows,listvariable=init_val)
# 追加初始值
for i in range(1,5):
    listbox.insert("end",i)
listbox.pack()

windows.mainloop()
