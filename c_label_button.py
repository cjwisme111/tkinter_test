# -*- coding: utf-8 -*-

from tkinter import Tk, Label,LEFT,W,Button,PhotoImage


# label 创建使用案例
def main_label():
    # 声明一个应用主窗口
    root = Tk()
    # 设置窗口大小 widthxheigth
    # root.geometry("200x100")
    # 标题
    root.title("my first tk")
    long_text = """
    hello
    world
    """
    Label(root,text=long_text,justify="center", anchor="nw").pack()
    root.mainloop()

def callback(val):
    print(val)
    print("回调函数")

def main_button():
    root = Tk()
    # Button(root,text="点我", command=callback).pack()
    # 传参
    # Button(root,text="点我", command=lambda : callback("hello")).pack()
    photo = PhotoImage(file=r"E:\demo\intel\timg.gif")
    # compound: 让文字显示的位置
    Button(root,text="点我",image=photo, compound = "center",font=20,fg="black").pack()

    root.mainloop()

if __name__ == "__main__":
    # main_label()
    main_button()