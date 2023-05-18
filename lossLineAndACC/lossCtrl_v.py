import csv

# 创建一个二维列表
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 将二维列表保存到文件中
with open('my_list.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(my_list)

import numpy as np

# 创建一个二维列表
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# 将二维列表保存到文件中
np.savetxt('my_list.txt', my_list)

# 打开文件并将其读取到一个字符串列表中
with open('my_list.txt', 'r') as f:
    lines = f.readlines()

# 使用列表推导式和 split() 方法将字符串拆分为一个内部列表
my_list = [line.strip().split() for line in lines]

# 打印二维列表
print(my_list)

import matplotlib.pyplot as plt

# 创建一个二维列表
loss = [[0.5, 0.3, 0.2, 0.15, 0.1], [0.4, 0.2, 0.1, 0.08, 0.05], [0.3, 0.15, 0.08, 0.05, 0.03]]

# 创建 x 轴的标签
x = range(1, len(loss[0]) + 1)

# 循环绘制 loss 曲线
for i in range(len(loss)):
    plt.plot(x, loss[i], label=f'loss{i+1}')

# 添加图例
plt.legend()

# 设置 x 轴和 y 轴标签以及标题
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Loss')

# 显示图形
plt.show()