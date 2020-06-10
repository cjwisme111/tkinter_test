# -*- coding: utf-8 -*-

from tkinter import Tk

from tkinter_test.a_v2_demo.LoginPage import LoginPage


def main():
    root = Tk()
    root.title('小程序')
    LoginPage(root)
    root.mainloop()

if __name__ == "__main__":
    main()