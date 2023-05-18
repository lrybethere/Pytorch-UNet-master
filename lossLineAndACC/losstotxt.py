# 假设 loss 值存储在名为 loss 的列表中
loss = [0.5, 0.3, 0.2, 0.15, 0.1]

# 将 loss 值保存到文本文件中
with open('loss.txt', 'w') as f:
    for item in loss:
        f.write(str(item) + '\n')