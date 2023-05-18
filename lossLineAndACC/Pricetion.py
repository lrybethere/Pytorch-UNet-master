from sklearn.metrics import precision_recall_curve
import matplotlib.pyplot as plt
import cv2
import numpy as np
# y_true是真实结果，y_pred是模型预测结果
y_true=np.array(cv2.imread(r'C:\Users\74408\Desktop\unet\pytorch-unet-master\data\SegmentationClass\1.png'))
y_true[y_true == 128] = 1

y_pred=np.array(cv2.imread(r'C:\Users\74408\Desktop\unet\pytorch-unet-master\data\SegmentationClass\1.png'))
y_pred[y_pred == 128] = 1

precision, recall, thresholds = precision_recall_curve(y_true.ravel(), y_pred.ravel())

# 绘制Precision-Recall曲线
plt.plot(recall, precision, 'b', label='Precision-Recall curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.ylim([0.0, 1.05])
plt.xlim([0.0, 1.0])
plt.title('Precision-Recall curve')
plt.legend(loc='lower left')
plt.show()

from sklearn.metrics import precision_score

# 将预测结果进行阈值化处理，得到二分类结果
thresholds = [i / 10.0 for i in range(11)]
y_pred_binary = [(y_pred >= t).astype(int) for t in thresholds]

# 计算每个阈值下的TP和FP，并计算Precision值
precisions = []
for y_pred_i in y_pred_binary:
    precision_i = precision_score(y_true.ravel(), y_pred_i.ravel())
    precisions.append(precision_i)
