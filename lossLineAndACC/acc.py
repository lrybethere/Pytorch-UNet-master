
from sklearn.metrics import accuracy_score

# 定义真实标签和预测标签
y_true = [1, 1, 0, 1, 0, 0, 1, 0]
y_pred = [1, 0, 0, 1, 1, 0, 1, 0]

# 计算精确度
acc = accuracy_score(y_true, y_pred)

# 打印精确度
print("Accuracy:", acc)
