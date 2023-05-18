import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# 读取文件并将数据转换为numpy数组
y_true = np.loadtxt('y_true.txt')
y_pred = np.loadtxt('y_pred.txt')
y_scores = np.loadtxt('y_scores.txt')

y_true = np.where(y_true > 0.5, 1, 0)
y_pred = np.where(y_pred > 0.5, 1, 0)
# a压缩到0-1之间
y_scores = (y_scores - y_scores.min()) / (y_scores.max() - y_scores.min())

# 计算混淆矩阵
tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

# 计算iou和acc
iou = tp / (tp + fp + fn)
acc = (tp + tn) / (tp + tn + fp + fn)

# 输出iou和acc
print('iou:', iou)
print('acc:', acc)

# 绘制iou和acc曲线
plt.plot([0, 1], [0, 1], 'k--')
plt.plot(y_scores, y_true, label='ROC curve (area = %0.2f)' % iou)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()

plt.plot([0, 1], [0, 1], 'k--')
plt.plot(y_scores, y_pred, label='Accuracy (area = %0.2f)' % acc)
plt.xlabel('Threshold')
plt.ylabel('Accuracy')
plt.title('Accuracy-Threshold Curve')
plt.legend(loc="lower right")
plt.show()
