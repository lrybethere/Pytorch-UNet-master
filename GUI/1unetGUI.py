'''写一个美观的unet网络训练界面，要求：两个参数输入epochs和learn，选择模型显示文件内容，按钮开始训练，实时输出训练迭代图，按钮开始测试，选择测试图片，输出预测图，按钮退出'''

import tkinter as tk
from PySimpleGUI import Image
from tkinter import filedialog, ttk

from PIL import Image


class UNetTrainerGUI:

    def __init__(self, master):

        self.master = master
        master.title("UNet网络训练")

        # 创建参数输入框
        self.epochs_label = tk.Label(master, text="训练epochs:")
        self.epochs_label.grid(row=0, column=0, padx=10, pady=10)
        self.epochs_entry = tk.Entry(master)
        self.epochs_entry.grid(row=0, column=1, padx=10, pady=10)

        self.learn_label = tk.Label(master, text="学习率:")
        self.learn_label.grid(row=1, column=0, padx=10, pady=10)
        self.learn_entry = tk.Entry(master)
        self.learn_entry.grid(row=1, column=1, padx=10, pady=10)

        # 创建选择模型按钮
        self.model_button = ttk.Button(master, text="选择模型", command=self.choose_model)
        self.model_label = ttk.Label(master, text="未选择模型文件")
        self.model_button.grid(row=2, column=0, padx=10, pady=10)
        self.model_label.grid(row=2, column=1, padx=10, pady=10)

        # 创建训练和测试按钮
        self.train_button = ttk.Button(master, text="开始训练", command=self.train)
        self.train_button.grid(row=3, column=0, padx=10, pady=10)

        self.test_button = ttk.Button(master, text="开始测试", command=self.test)
        self.test_button.grid(row=3, column=1, padx=10, pady=10)

        # 创建实时输出训练迭代图
        self.train_image_label = tk.Label(master)
        self.train_image_label.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

        # 创建选择测试图片按钮
        self.test_image_button = ttk.Button(master, text="选择测试图片", command=self.choose_test_image)
        self.test_image_button.grid(row=5, column=0, padx=10, pady=10)

        # 创建输出预测图
        self.prediction_image_label = tk.Label(master)
        self.prediction_image_label.grid(row=6, column=0, padx=10, pady=10, columnspan=2)

        # 创建测试图片label
        self.test_image_label = ttk.Label(master)
        self.test_image_label.grid(row=7, column=0, padx=10, pady=10, columnspan=2)

        # 创建退出按钮
        self.quit_button = ttk.Button(master, text="退出", command=master.quit)
        self.quit_button.grid(row=8, column=0, padx=10, pady=10, columnspan=2)


    def choose_model(self):
        # TODO: 选择模型并显示文件内容
        model_file = filedialog.askopenfilename()

        # 如果选择了模型文件，则将文件名显示在Label上，并显示文件内容
        if model_file:
            self.model_label.config(text=model_file)
            with open(model_file, 'r') as f:
                model_content = f.read()
            # 创建显示模型内容的文本框
            self.model_text = tk.Text(self.master, height=10, width=50)
            self.model_text.insert(tk.END, model_content)
            self.model_text.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        pass

    def train(self):
        # TODO: 实现训练功能，输出实时训练迭代图
        pass

    def test(self):
        # TODO: 实现测试功能，选择测试图片并输出预测图
        pass

    def choose_test_image(self):
        # TODO: 选择测试图片
        # 弹出文件选择对话框，获取用户选择的文件路径
        test_image_path = filedialog.askopenfilename(initialdir="./", title="选择测试图片",
                                                     filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if test_image_path:
            # 加载测试图片
            self.test_image = Image.open(test_image_path)
            # 在GUI上显示测试图片
            self.test_image_label.config(image=self.test_image)
            self.test_image_label.image = self.test_image
        pass

if __name__ == "__main__":
    root = tk.Tk()
    gui = UNetTrainerGUI(root)
    root.mainloop()
