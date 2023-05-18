import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class ImageApp:
    def __init__(self, master):
        self.master = master
        master.title("Image App")
        master.geometry("400x400")
        master.resizable(False, False)

        # 创建一个Button用于打开图片
        self.button_open = tk.Button(master, text="打开图片", command=self.open_image)
        self.button_open.pack(pady=10)

        # 创建一个Listbox用于显示文件夹内容
        self.listbox_files = tk.Listbox(master)
        self.listbox_files.pack(pady=10)

        # 显示文件夹内容
        self.refresh_file_list()

        # 初始化当前图片
        self.current_image = None

    def open_image(self):
        # 打开文件选择对话框
        file_path = filedialog.askopenfilename()

        if file_path:
            # 打开选择的图片文件
            image = Image.open(file_path)

            # 把图片转换成Tkinter所需的格式
            tk_image = ImageTk.PhotoImage(image)

            # 更新Label中显示的图片
            self.label.configure(image=tk_image)

            # 保留对当前图片的引用，避免被垃圾回收器回收
            self.current_image = tk_image

    def refresh_file_list(self):
        # 清空Listbox
        self.listbox_files.delete(0, tk.END)

        # 获取当前文件夹中的所有文件名
        folder_path = os.getcwd()
        file_names = os.listdir(folder_path)

        # 将所有文件名添加到Listbox中
        for name in file_names:
            self.listbox_files.insert(tk.END, name)

# 创建一个Tkinter窗口并运行主事件循环
root = tk.Tk()
app = ImageApp(root)
root.mainloop()
