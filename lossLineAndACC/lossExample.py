import matplotlib.pyplot as plt


# 打开文件并将其读取到一个字符串列表中

with open(r'C:\Users\74408\Desktop\unet\pytorch-unet-master\loss_every_epoch100.txt', 'r') as f:
    my_array = [float(line.strip()) for line in f.readlines()]



# 打印二维列表
print(my_array)

# 创建一个数组来保存损失函数的值
# loss_values = [0.2, 0.15, 0.1, 0.08, 0.06, 0.05, 0.04, 0.03, 0.02, 0.01]
loss_values=my_array
# 创建 x 轴上的值，这里用迭代器生成
x_values = range(len(loss_values))

# 绘制曲线
plt.plot(x_values, loss_values, label='Loss Curve')

# 添加标签
plt.xlabel('epoch/per100')
plt.ylabel('Loss')
plt.title('Training Loss Curve')

# 显示图像
plt.legend()
plt.show()
