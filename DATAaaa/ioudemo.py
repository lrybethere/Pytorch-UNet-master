import matplotlib.pyplot as plt

# 读取 HEDiou.txt 文件
with open('HEDiou.txt', 'r') as f:
    hed_iou_list = [float(line.strip()) for line in f.readlines()]

# 读取 iou.txt 文件
with open('iou.txt', 'r') as f:
    iou_list = [float(line.strip()) for line in f.readlines()]

# 绘制 IoU 曲线
plt.figure(figsize=(8, 6))
plt.plot(hed_iou_list, label='HED IoU')
plt.plot(iou_list, label='IoU')
plt.legend(loc='lower right')
plt.title('Epoch-IoU Comparison')
plt.xlabel('Epoch')
plt.ylabel('IoU')
plt.show()
