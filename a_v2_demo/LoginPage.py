# -*- coding: utf-8 -*-

from tkinter import StringVar,Frame,Label,Button,Entry,W,E
from tkinter.messagebox import showerror

from tkinter_test.a_v2_demo.MainPage import MainPage
from tkinter_test.a_v2_demo import constants


class LoginPage(object):

    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.geometry('%dx%d' % (constants.PARAMS_WIDTH, constants.PARAMS_HEIGHT))  # 设置窗口大小
        self.p1 = StringVar(value=constants.PARAMS_1)
        self.p2 = StringVar(value=constants.PARAMS_2)
        self.p3 = StringVar(value=constants.PARAMS_3)
        self.p4 = StringVar(value=constants.PARAMS_4)
        self.create_page()

    def create_page(self):
        self.page = Frame(self.root)  # 创建Frame
        self.page.pack()
        Label(self.page).grid(row=0, stick=W)

        Label(self.page, text='参数一: ').grid(row=1, stick=W, pady=10)
        Entry(self.page, textvariable=self.p1).grid(row=1, column=1, stick=E)

        Label(self.page, text='参数二: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.p2).grid(row=2, column=1, stick=E)

        Label(self.page, text='参数三: ').grid(row=3, stick=W, pady=10)
        Entry(self.page, textvariable=self.p3).grid(row=3, column=1, stick=E)

        Label(self.page, text='参数四: ').grid(row=4, stick=W, pady=10)
        Entry(self.page, textvariable=self.p4).grid(row=4, column=1, stick=E)

        Button(self.page, text='确认', command=self.login_check).grid(row=5, stick=W, pady=10)
        Button(self.page, text='退出', command=self.page.quit).grid(row=5, column=1, stick=E)

    def login_check(self):
        p1 = self.p1.get()
        p2 = self.p2.get()
        p3 = self.p3.get()
        p4 = self.p4.get()

        if not all((p1, p2, p3, p4)):
            # 弹出错误信息
            showerror(title='错误', message='必填参数')
        else:
            # 跳转下一个页面
            self.page.destroy()
            kwargs = {
                "p1":p1,
                "p2":p2,
                "p3":p3,
                "p4":p4,
            }
            MainPage(self.root, **kwargs)


