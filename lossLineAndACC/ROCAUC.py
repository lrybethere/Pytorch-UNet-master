import numpy as np
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt

# 从文本文件中读取 y_true 和 y_scores
y_true = np.loadtxt('y_true.txt')
y_scores = np.loadtxt('y_scores.txt')

# 计算 ROC 曲线和 AUC 值
fpr, tpr, _ = roc_curve(y_true, y_scores)
roc_auc = auc(fpr, tpr)

# 绘制 ROC 曲线
plt.figure()
plt.plot(fpr, tpr, color='darkorange', lw=2, label='ROC curve (AUC = %0.2f)' % roc_auc)
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver operating characteristic')
plt.legend(loc="lower right")
plt.show()
