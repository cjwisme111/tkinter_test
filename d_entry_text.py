# -*- coding: utf-8 -*-

import tkinter as tk

windows = tk.Tk()
windows.title("entry and text test")
windows.geometry("200x200")

# entry 输入控件，show 展示的信息，
entry = tk.Entry(windows,show=None)

def insert_point():
    var = entry.get()
    t.insert("insert",var)

def insert_end():
    var = entry.get()
    t.insert("end",var)

b_1 = tk.Button(windows, text="insert point", width=10, height=2, bg="yellow",command=insert_point)

b_2 = tk.Button(windows, text="insert end", width=10, height=2, bg="blue",command=insert_end)

t = tk.Text(windows,height=5)

entry.pack()
b_1.pack()
b_2.pack()
t.pack()

windows.mainloop()