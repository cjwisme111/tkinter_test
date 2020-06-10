# -*- coding: utf-8 -*-

from tkinter import Menu

# 菜单栏对应的各个子页面
from tkinter_test.a_v2_demo.views import NewProjectFrame,NewFrame,CopyFrame,TypeInfoFrame,BackFrame
from tkinter_test.a_v2_demo import constants


class MainPage(object):

    def __init__(self, master=None, *args, **kwargs):
        self.root = master  # 定义内部变量root
        self.data = {}
        self.args = args
        self.kwargs = kwargs
        self.root.geometry('%dx%d' % (constants.MAIN_WIDTH, constants.MAIN_HEIGHT))  # 设置窗口大小
        self.createPage()

    def create_frame(self):
        """
        创建frame
        :return: None
        """
        self.data["new_project_page"] = NewProjectFrame(self.root, *self.args, **self.kwargs)
        self.data["new_page"] = NewFrame(self.root, *self.args, **self.kwargs)
        self.data["copy_page"] = CopyFrame(self.root, *self.args, **self.kwargs)
        self.data["type_info_page"] = TypeInfoFrame(self.root, *self.args, **self.kwargs)
        self.data["back_page"] = BackFrame(self.root, *self.args, **self.kwargs)

        # 默认的页面
        self.data["new_project_page"].pack()

    def createPage(self):
        """创建页面"""
        self.create_frame()
        self.menu()

    def menu(self):
        """生成菜单"""
        menubar = Menu(self.root)
        file_menu = Menu(menubar, tearoff=False)
        # file_menu.add_command(label="New Project", command=self.new_project_data)
        file_menu.add_command(label="New Project", command=lambda :self.show_page("new_project_page"))
        file_menu.add_command(label="New", command=lambda :self.show_page("new_page"))
        menubar.add_cascade(label="File", menu=file_menu)

        edit_menu = Menu(menubar, tearoff=False)
        edit_menu.add_command(label="Copy", command=lambda :self.show_page("copy_page"))
        menubar.add_cascade(label="Edit", menu=edit_menu)

        view_menu = Menu(menubar, tearoff=False)
        view_menu.add_command(label="Type Info", command=lambda :self.show_page("type_info_page"))
        menubar.add_cascade(label="View", menu=view_menu)

        nav_menu = Menu(menubar, tearoff=False)
        nav_menu.add_command(label="Back", command=lambda :self.show_page("back_page"))
        menubar.add_cascade(label="Navigate", menu=nav_menu)

        # 设置菜单栏
        self.root['menu'] = menubar

    def show_page(self, page_name):
        for k in self.data.keys():
            if page_name == k:
                self.data[k].pack()
            else:
                self.data[k].pack_forget()
