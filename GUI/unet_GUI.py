"""
测试一个经典的GUI程序
使用面向对象的方式
"""

from tkinter import *
from tkinter import messagebox


class Application(Frame):
    """
    一个经典的GUI程序的类的写法
    """

    def __init__(self, master=None):  # 构造器：用来构造组件对象
        super().__init__(master)
        self.master = master
        self.pack()

        self.createWidge()

    def createWidge(self):  # 如果有很多个组件，可以单独定义一个方法
        """
        创建新的组件
        """
        self.btn01 = Button(self)

        self.btn01["text"] = "开始训练"
        self.btn01.pack()  # 通过布局管理器显示
        self.btn01["command"] = self.songhua  # 加事件

        # 创建一个退出按钮
        self.btnQuit = Button(self, text="退出", command=root.destroy)
        self.btnQuit.pack()

    def songhua(self):
        messagebox.showinfo("train", "run.....")


if __name__ == '__main__':
    root = Tk()  # 创建一个根窗口对象
    root.geometry("800x500+200+300")
    root.title("基于U-net矿石图像分割算法图形界面")
    app = Application(master=root)
    root.mainloop()