import numpy as np
from sklearn.metrics import precision_recall_curve, average_precision_score
import matplotlib.pyplot as plt

# 从文本文件中读取 y_scores 和 y_pred
y_scores = np.loadtxt(r'C:\Users\74408\Desktop\unet\pytorch-unet-master\y_scores.txt')
y_true = np.loadtxt(r'C:\Users\74408\Desktop\unet\pytorch-unet-master\y_pred.txt')
y_pred = np.loadtxt(r'C:\Users\74408\Desktop\unet\pytorch-unet-master\y_pred.txt')

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, confusion_matrix

# 将多标签指示器转换为一维数组
y_scores = np.argmax(y_scores, axis=1)
y_true = np.argmax(y_true, axis=1)
y_pred = np.argmax(y_pred, axis=1)
y_scores = y_scores.ravel()



# 计算 confusion matrix
cm = confusion_matrix(y_true, y_pred)

# 计算 TP, FP, TN, FN
TP = np.diag(cm)
FP = np.sum(cm, axis=0) - TP
FN = np.sum(cm, axis=1) - TP
TN = np.sum(cm) - (TP + FP + FN)

# 计算 IoU
IoU = TP / (TP + FP + FN)

# 计算 accuracy
acc = accuracy_score(y_true, y_pred)

# 绘制 IoU 和 accuracy 曲线
thresholds = np.linspace(0, 1, 100)
iou_curve = [IoU[y_scores > t].mean() for t in thresholds]
acc_curve = [accuracy_score(y_true[y_scores > t], y_pred[y_scores > t]) for t in thresholds]

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(thresholds, iou_curve, 'b-')
ax2.plot(thresholds, acc_curve, 'r-')

ax1.set_xlabel('Threshold')
ax1.set_ylabel('IoU', color='b')
ax2.set_ylabel('Accuracy', color='r')

plt.show()
