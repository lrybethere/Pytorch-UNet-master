import pickle

# 创建一个数组
my_array = [1, 2, 3, 4, 5,44]
# 该文件是以二进制模式打开的（即 'wb'），以便正确写入二进制数据。
# 将数组保存到文件中
with open('my_array.pickle', 'wb') as f:
    pickle.dump(my_array, f)
import pickle

# 从文件中加载数组
with open('my_array.pickle', 'rb') as f:
    my_array = pickle.load(f)

# 打印数组
print(my_array)

