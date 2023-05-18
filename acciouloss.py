import numpy as np
import matplotlib.pyplot as plt

# 读取文件
with open('iou.txt', 'r') as f:
    iou_list = [float(line.strip()) for line in f.readlines()]

with open('acc.txt', 'r') as f:
    acc_list = [float(line.strip()) for line in f.readlines()]

with open('loss_list.txt', 'r') as f:
    loss_list = [float(line.strip()) for line in f.readlines()]

# 绘制曲线
plt.figure(figsize=(8, 6))

# 绘制loss-epoch曲线
# 设置纵轴范围
plt.ylim(0.1, 1.0)
plt.plot(loss_list, label='loss')
plt.legend(loc='lower right')
plt.title('Test loss-NO.')
plt.xlabel('NO.')
plt.ylabel('loss')
plt.show()

# 绘制acc-epoch曲线
# 设置纵轴范围
plt.ylim(0.1, 1.0)
plt.plot(acc_list, label='acc')
plt.legend(loc='lower right')
plt.title('Test accuracy-NO.')
plt.xlabel('NO.')
plt.ylabel('accuracy')
plt.show()

# 绘制iou-epoch曲线
# 设置纵轴范围
plt.ylim(0.1, 1.0)
plt.plot(iou_list, label='iou')
plt.legend(loc='lower right')
plt.title('Test iou-NO.')
plt.xlabel('NO.')
plt.ylabel('iou')
plt.show()


