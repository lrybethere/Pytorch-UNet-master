import tkinter as tk
from PySimpleGUI import Image
from tkinter import *
from tkinter import filedialog, ttk
from tkinter import messagebox

from PIL import ImageTk
from torch import optim
from torch.utils.data import DataLoader
from torchvision.utils import save_image

from data import *
from net import *


class UNetTrainerGUI:
    def __init__(self, master):

        weights = r'C:\Users\74408\Desktop\unet\pytorch-unet-master\params/unet.pth'
        if os.path.exists(weights):
            self.model = UNet().cpu()  #
            self.model.load_state_dict(torch.load(weights))
            print('successfully')
        else:
            print('no loading')

        self.master = master
        master.title("U-net ore image segmentation system")


        # 创建输入epochs和learn的label和entry
        ttk.Label(master, text="Epochs:").grid(row=0, column=0, padx=10, pady=10)
        self.epochs_entry = ttk.Entry(master)
        self.epochs_entry.grid(row=0, column=1, padx=10, pady=10)
        ttk.Label(master, text="Learn rate:").grid(row=1, column=0, padx=10, pady=10)
        self.learn_rate_entry = ttk.Entry(master)
        self.learn_rate_entry.grid(row=1, column=1, padx=10, pady=10)

        # 创建选择模型的按钮和显示文件内容的label
        self.model_file_label = ttk.Label(master, text="Select weights：")
        self.model_file_label.grid(row=2, column=0, padx=10, pady=10)
        self.model_file_button = ttk.Button(master, text="select", command=self.choose_model)
        self.model_file_button.grid(row=2, column=1, padx=10, pady=10)

        # 创建训练和测试按钮，开始测试按钮
        self.train_button = ttk.Button(master, text="started training", command=self.train)
        self.train_button.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

        self.test_image_button = ttk.Button(master, text="Select Test Image", command=self.choose_test_image)
        self.test_image_button.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

        self.test_begin_button = ttk.Button(master, text="start test", command=self.predict)
        self.test_begin_button.grid(row=4, column=2, padx=10, pady=10, columnspan=2)



        # 创建显示训练迭代图和预测图的label
        self.train_image_tk = ImageTk.PhotoImage(Image.new("RGB", (300, 300), "white"))
        self.train_image_label = ttk.Label(master, image=self.train_image_tk)
        self.train_image_label.grid(row=5, column=0, padx=10, pady=10, columnspan=2)

        self.test_image_tk = ImageTk.PhotoImage(Image.new("RGB", (300, 300), "white"))
        self.test_image_label = ttk.Label(master, image=self.test_image_tk)
        self.test_image_label.grid(row=5, column=2, padx=10, pady=10, columnspan=2)

        self.stop_training = False  # 标志用于检查用户是否要中止训练

        # 创建“跳出”按钮
        self.stop_button = tk.Button(self.master, text='Stop Training',command=self.stop_train)
        self.stop_button.grid(row=3, column=2, padx=10, pady=10, columnspan=2)

        # 创建退出按钮
        self.quit_button = ttk.Button(master, text="exit", command=master.quit)
        self.quit_button.grid(row=8, column=0, padx=10, pady=10, columnspan=2)

    def choose_model(self):
        # 选择模型并显示文件内容
        model_file_path = filedialog.askopenfilename(initialdir="./", title="ww")
    def stop_train(self):
        #循环点击事件
        if self.stop_training:
            self.stop_training=False
            print("self.stop_button=False")
        else:
            self.stop_training = True  # 设置标志以停止训练
            print("self.stop_training = True  # 设置标志以停止训练")

    def predict(self):
        # TODO: 实现预测功能，输出预测图
        if not self.test_image:
            messagebox.showwarning("警告", "请先选择测试图片")
            return

        # 将测试图片转换为模型输入格式

        self.test_image = keep_image_size_read(self.test_image)
        img_data = transform(self.test_image).cpu()
        print(img_data.shape)
        img_data = torch.unsqueeze(img_data, dim=0)
        output = self.model(img_data)
        #保存
        save_image(output, r'C:\Users\74408\Desktop\unet\pytorch-unet-master\result/rGUI.png')
        # 将预测图转换为Image格式，并在GUI上显示
        output = Image.open(r'C:\Users\74408\Desktop\unet\pytorch-unet-master\result/rGUI.png')

        predicted_image_tk = ImageTk.PhotoImage(output, width=256, height=256)
        self.train_image_label.config(image=predicted_image_tk)
        self.train_image_label.image = predicted_image_tk



    def train(self):
        # 获取epochs和learn参数的值
        # epochs = self.epochs_var.get()
        # learn = self.learn_var.get()
        # TODO: 实现训练功能，输出实时训练迭代图

        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')  # 设备
        weight_path = r'C:\Users\74408\Desktop\unet\pytorch-unet-master\params\unet.pth'
        data_path = r'C:\Users\74408\Desktop\unet\pytorch-unet-master\data'  ##这里输入训练图片路径
        save_path = r'C:\Users\74408\Desktop\unet\pytorch-unet-master\train_image'
        data_loader = DataLoader(MyDataset(data_path), batch_size=2, shuffle=True)
        net = UNet().to(device)
        if os.path.exists(weight_path):
            net.load_state_dict(torch.load(weight_path))
            print('successful load weight！')
        else:
            print('not successful load weight')

        # 优化函数adam
        lr = 1e-4
        opt = optim.Adam(net.parameters(), lr=lr)
        loss_fun = nn.BCELoss()
        # loss初值 +无穷
        best_loss = float('inf')

        epoch = 1
        while True:
            if self.stop_training:  # 检查是否要中止训练
                break
            for i, (image, segment_image) in enumerate(data_loader):
                if self.stop_training:  # 检查是否要中止训练
                    break
                image, segment_image = image.to(device), segment_image.to(device)
                out_image = net(image)
                train_loss = loss_fun(out_image, segment_image)
                opt.zero_grad()
                train_loss.backward()
                opt.step()
                # print(len(data_loader))
                print(i)
                if i % 10 == 0:  # 输出
                    print(f'{epoch}-{i}-train_loss===>>{train_loss.item()}')
                # if i%50==0:#保存权重
                if train_loss.item() < best_loss:
                    best_loss = train_loss.item()
                    torch.save(net.state_dict(), weight_path)
                    print("保存权重")
                # if i % 7 == 0:
                _image = image[0]
                _segment_image = segment_image[0]
                _out_image = out_image[0]
                img = torch.stack([_image, _segment_image, _out_image], dim=0)
                # save_image(img, f'{save_path}/{i}.png')
                save_image(img, fr'C:\Users\74408\Desktop\unet\pytorch-unet-master\train_image\00.png')

                # 并输出迭代图
                # 创建一个canvas用于显示训练迭代图
                self.train_canvas = tk.Canvas(self.master, width=800, height=300)
                self.train_canvas.grid(row=5, column=0, padx=10, pady=10, rowspan=4)
                # self.train_canvas.pack()
                image = tk.PhotoImage(file=r'C:\Users\74408\Desktop\unet\pytorch-unet-master\train_image\00.png')
                self.train_canvas.create_image(0, 0, anchor='nw', image=image)
                self.train_canvas.update()
            epoch += 1



    def choose_test_image(self):
        # TODO: 选择测试图片
        # 弹出文件选择对话框，获取用户选择的文件路径
        test_image_path = filedialog.askopenfilename(initialdir="./", title="选择测试图片",
                                                     filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
        if test_image_path:
            # 加载测试图片
            self.test_image = Image.open(test_image_path)
            # 在GUI上显示测试图片
            img=self.test_image
            img.thumbnail((256, 256))
            self.test_image_tk = ImageTk.PhotoImage(img,width=256, height=256)
            self.test_image_label.config(image=self.test_image_tk)
            self.test_image_label.image = self.test_image_tk

    def quit(self):
        # TODO: 实现退出功能
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    gui = UNetTrainerGUI(root)
    root.mainloop()


''' 3gui 中将会把迭代图放到新的的地方'''