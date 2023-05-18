import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk


class ModelTrainer:
    def __init__(self, master):
        self.master = master
        master.title("基于U-net矿石图像分割算法图形化界面")
        master.resizable(False, False)

        style = ttk.Style()
        style.configure('TButton', font=('Arial', 12), foreground='black', background='#4CAF50')
        style.configure('TLabel', font=('Arial', 12))
        style.configure('TEntry', font=('Arial', 12))

        self.dataset_path = r'C:\Users\74408\Desktop\unet\pytorch-unet-master\data'
        self.weights_path = r'C:\Users\74408\Desktop\unet\pytorch-unet-master\params\unet.pth'

        # 选择数据集控件
        self.dataset_label = ttk.Label(master, text="数据集路径：", anchor='w')
        self.dataset_label.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.dataset_path_label = ttk.Label(master, text="")
        self.dataset_path_label.grid(row=0, column=1, padx=10, pady=10, sticky='w')

        self.dataset_button = ttk.Button(master, text="选择数据集", command=self.choose_dataset)
        self.dataset_button.grid(row=0, column=2, padx=10, pady=10)

        # 网络参数控件
        self.network_label = ttk.Label(master, text="网络参数：", anchor='w')
        self.network_label.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        self.network_entry = ttk.Entry(master, width=50)
        self.network_entry.grid(row=1, column=1, padx=10, pady=10, sticky='w')

        # 训练控件
        self.train_button = ttk.Button(master, text="开始训练", command=self.train_model)
        self.train_button.grid(row=2, column=0, padx=10, pady=10)

        # 选择权重控件
        self.weights_label = ttk.Label(master, text="权重文件：", anchor='w')
        self.weights_label.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        self.weights_path_label = ttk.Label(master, text="")
        self.weights_path_label.grid(row=3, column=1, padx=10, pady=10, sticky='w')

        self.weights_button = ttk.Button(master, text="选择权重", command=self.choose_weights)
        self.weights_button.grid(row=3, column=2, padx=10, pady=10)

        # 测试控件
        self.test_button = ttk.Button(master, text="开始测试", command=self.test_model)
        self.test_button.grid(row=4, column=0, padx=10, pady=10)

        # 图片控件
        self.image_label = ttk.Label(master, text="测试图片：", anchor='w')
        self.image_label.grid(row=5, column=0, padx=10, pady=10, sticky='w')

        self.image_path_label = ttk.Label(master, text="")
        self.image_path_label.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        self.image_button = ttk.Button(master, text="选择图片", command=self.choose_image)
        self.image_button.grid(row=5, column=2, padx=10, pady=10)

        self.image_canvas = tk.Canvas(master, width=224, height=244)
        # 图片控件
        self.image_label = ttk.Label(master, text="测试图片：", anchor='w')
        self.image_label.grid(row=5, column=0, padx=10, pady=10, sticky='w')

        self.image_path_label = ttk.Label(master, text="")
        self.image_path_label.grid(row=5, column=1, padx=10, pady=10, sticky='w')

        self.image_button = ttk.Button(master, text="选择图片", command=self.choose_image)
        self.image_button.grid(row=5, column=2, padx=10, pady=10)

        self.image_canvas = tk.Canvas(master, width=224, height=224, bg='#EEEEEE')
        self.image_canvas.grid(row=6, column=0, columnspan=3, padx=10, pady=10)


    def choose_dataset(self):
        self.dataset_path = filedialog.askdirectory()
        self.dataset_path_label.configure(text=self.dataset_path)

    def choose_weights(self):
        self.weights_path = filedialog.askopenfilename()
        self.weights_path_label.configure(text=self.weights_path)

    def choose_image(self):
        image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.jpeg;*.png")])
        if image_path:
            self.image_path_label.configure(text=image_path)
            self.show_image(image_path)

    def show_image(self, image_path):
        image = Image.open(image_path)
        image = image.resize((224, 224), Image.ANTIALIAS)
        photo = ImageTk.PhotoImage(image)
        self.image_canvas.delete("all")
        self.image_canvas.create_image(0, 0, anchor='nw', image=photo)
        self.image_canvas.image = photo

    def train_model(self):
        # 获取网络参数并开始训练
        pass

    def test_model(self):
        # 使用选择的权重文件进行测试并显示输出图片
        pass
root = tk.Tk()
app = ModelTrainer(root)
root.mainloop()