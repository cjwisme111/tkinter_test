# -*- coding:utf-8 -*-


class FrameMixin:

    def __init__(self, master, *args, **kwargs):
        super().__init__(master)
        self.args = args
        self.kwargs = kwargs
        # 页面初始化参数
        self.init(master)
        self.create_page()