# -*- coding: utf-8 -*-

import tkinter as tk

# 声明一个应用主窗口
windows = tk.Tk()
# 设置窗口大小 widthxheigth
windows.geometry("200x100")
# 标题
windows.title("my first tk")

var1 = tk.StringVar()
on_line = True
def show_label():
    global on_line
    if on_line:
        var1.set("hit me")
        on_line = False
    else:
        var1.set("")
        on_line = True

# label
l = tk.Label(windows,textvariable=var1, state="disable",background="yellow",font="Arial",underline=1)
# 按钮
# command : callback 回调方法
b = tk.Button(windows,height=2,width=10,text="hit me",bg="green",command=show_label)
l.pack()
b.pack()
windows.mainloop()
