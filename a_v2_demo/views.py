# -*- coding:utf-8 -*-

from tkinter import Label,Button,StringVar,Entry,Frame,W

from tkinter_test.a_v2_demo.mixins import FrameMixin
from tkinter_test.a_v2_demo.exceptions import InitException,PageException


class BaseFrame:

    def init(self):
        raise InitException("init() error")

    def create_page(self):
        raise PageException("create_page() error")


class NewProjectFrame(BaseFrame, FrameMixin, Frame):

    def init(self, master):
        self.root = master  # 定义内部变量root
        self.path1 = StringVar(value=self.kwargs.get("p1"))
        self.path2 = StringVar(value=self.kwargs.get("p2"))
        self.path3 = StringVar(value=self.kwargs.get("p3"))
        self.path4 = StringVar(value=self.kwargs.get("p4"))
        self.importPrice = StringVar()

    def create_page(self):
        Label(self).grid(row=0, stick=W, pady=10)
        dic = {
            "path1": self.path1,
            "path2": self.path2,
            "path3": self.path3,
            "path4": self.path4,
        }
        self.create_label_entry(dic)
        self.run_but = Button(self, text="Run", width=8, command=self.run)
        self.run_but.grid(row=1, column=2, padx=5)
        self.pause_but = Button(self, text="Pause", width=8, command=self.pause)
        self.pause_but.grid(row=1, column=3, padx=5)
        self.stop_but = Button(self, text="stop", width=8, command=self.stop)
        self.stop_but.grid(row=1, column=4, padx=5)

    def create_label_entry(self, text2entry_dict):
        i = 1
        for text, val in text2entry_dict.items():
            Label(self, text=text).grid(row=i, stick=W, pady=10)
            Entry(self, width=30, textvariable=val).grid(row=i, column=1, stick=W)
            i += 1

    def run(self):
        """运行"""
        self.path1.set("running")
        self.run_but.config(state="disabled")
        self.pause_but.config(state="active")
        self.stop_but.config(state="active")
        print("run")

    def pause(self):
        """停止"""
        self.path1.set("stop")
        self.run_but.config(state="active")
        self.pause_but.config(state="disabled")
        self.stop_but.config(state="active")
        print("run")

    def stop(self):
        """显示到文本框"""
        item = self.path1.get()
        self.run_but.config(state="active")
        self.pause_but.config(state="active")
        self.stop_but.config(state="disabled")
        print(self.path1.get())


class NewFrame(BaseFrame, FrameMixin, Frame):

    def init(self, master):
        self.root = master  # 定义内部变量root

    def create_page(self):
        Label(self, text="New Page").pack()


class CopyFrame(FrameMixin, Frame):

    def init(self, master):
        self.root = master  # 定义内部变量root

    def create_page(self):
        Label(self, text="copy page").pack()


class TypeInfoFrame(FrameMixin, Frame):

    def init(self, master):
        self.root = master  # 定义内部变量root

    def create_page(self):
        Label(self, text="Type Info page").pack()


class BackFrame(FrameMixin, Frame):

    def init(self, master):
        self.root = master  # 定义内部变量root

    def create_page(self):
        Label(self, text="back page").pack()
