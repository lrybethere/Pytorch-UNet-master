"# pytorch-unet-master" 
"# pytorch-unet-master" 
# U-Net 矿石图像图像分割

本项目是一个使用 U-Net 网络进行图像分割的示例。U-Net 是一种深度学习网络结构，广泛应用于医学图像分割等任务。
本项目应用u-net对矿石图像进行图像分割

## 项目结构

- `data/`：存放训练和测试数据集
- `params/`：存放 U-Net 模型的定义和训练代码
- `utils/`：存放辅助函数和工具代码
- `DATA/`：存放评价标准的绘制曲线
- `GUI/`：存放简单的图形界面
- `README.md`：项目说明文件

## 数据集

本项目使用了一个自制数据集，用于训练和测试 U-Net 模型。数据集包括输入图像和对应的标签图像，用于图像分割任务。

## 模型训练

在 `models/` 目录下，我们提供了训练 U-Net 模型的代码。你可以运行 `train.py` 脚本来进行模型训练。训练完成后，模型参数将保存在 `params/` 目录下。

```bash
python train.py
```

## 训练迭代图


![0](https://github.com/lrybethere/pytorch-unet-master/assets/77471755/cb1a5bc8-2543-4066-84b2-16aef84dc427)


## 作者邮箱

744087051@qq.com
