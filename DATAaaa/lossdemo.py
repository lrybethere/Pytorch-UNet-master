import matplotlib.pyplot as plt

# 读取HEDloss_list.txt的loss数据
with open('HEDloss_list.txt', 'r') as f:
    HED_loss_list = [float(line.strip()) for line in f.readlines()]

# 读取loss_list.txt的loss数据
with open('loss_list.txt', 'r') as f:
    loss_list = [float(line.strip()) for line in f.readlines()]

# 绘制曲线
plt.figure(figsize=(8, 6))

# 绘制HED_loss曲线
plt.plot(HED_loss_list, label='HED_loss')

# 绘制loss_list曲线
plt.plot(loss_list, label='loss')

# 设置图例和标签
plt.ylim(0.1, 1.0)
plt.legend(loc='upper right')  # 将图例放置于右上角
plt.title('Epoch-Loss comparison')
plt.xlabel('Epoch')
plt.ylabel('Loss')

# 显示图形
plt.show()
