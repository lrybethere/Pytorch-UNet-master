import matplotlib.pyplot as plt

# 读取 HEDacc.txt 文件
with open('HEDacc.txt', 'r') as f:
    hed_acc_list = [float(line.strip()) for line in f.readlines()]

# 读取 acc.txt 文件
with open('acc.txt', 'r') as f:
    acc_list = [float(line.strip()) for line in f.readlines()]

# 绘制准确率曲线
plt.ylim(0.1, 1.0)

plt.figure(figsize=(8, 6))
plt.plot(hed_acc_list, label='HED Accuracy')
plt.plot(acc_list, label='Accuracy')
plt.legend(loc='lower right')
plt.title('Epoch-Accuracy comparison')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.show()
