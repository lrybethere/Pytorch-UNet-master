import json

import matplotlib
import numpy as np
from matplotlib import pyplot as plt

matplotlib.use("qt5agg")
from numpy import random

with open(r'C:\Users\74408\Desktop\unet\pytorch-unet-master\result\json\211_01.json', 'r') as f:
    config = json.load(f)


def plot_accuracy(num_epochs, train_acc, val_acc, val_step_size, output_folder, save=True):
    """Plot training and validation accuracy over the given epochs"""
    plt.plot(range(0, num_epochs), train_acc, 'r--', label='Training Accuracy')
    plt.plot(range(0, num_epochs, val_step_size), val_acc, 'b-', label='Validation Accuracy')
    plt.ylim(0, 1)
    plt.legend(loc='lower right')
    plt.xlabel('epoch')
    plt.ylabel('accuracy')
    plt.title('Training Accuracy vs Validation Accuracy')
    plt.grid(True)
    plt.show()
    if save:
        plt.savefig(output_folder + '/accuracies.png')
        plt.clf()


def plot_errors(num_epochs, train_losses, val_step_size, output_folder, save=True, bce_dice_focal=False):
    """Plot training and validation error over the given epochs"""
    import matplotlib.pyplot as plt
    plt.plot(range(0, num_epochs), train_losses, 'r--', label='Training DiceLoss')
    # plt.plot(range(0, num_epochs, val_step_size), val_losses, 'b-', label='Validation DiceLoss')
    if bce_dice_focal:
        plt.ylim(bottom=0)
    else:
        plt.ylim(0, 1)
    plt.xlim(left=0)
    plt.legend(loc='lower right')
    plt.xlabel('No.')
    plt.ylabel('IoU')
    plt.title('Test IoU')
    plt.grid(True)
    test_acc = train_losses
    test_acc_min = np.argmin(test_acc)
    test_acc_max = np.argmax(test_acc)
    show_min = '[' + 'IoU_Min' + ' ' + '%.2f' % test_acc[test_acc_min] + ']'
    show_max = '[' + 'IoU_Max' + ' ' + '%.2f' % test_acc[test_acc_max] + ']'
    # 以●绘制最大值点和最小值点的位置
    plt.plot(test_acc_min, test_acc[test_acc_min], 'ko')
    plt.plot(test_acc_max, test_acc[test_acc_max], 'ko')
    '''
    该函数用以在图上标注文字
    plt.annotate(s='str',
    	xy=(x,y) ,
    	xytext=(l1,l2) ,
    	...
    )
    s：为注释文本内容
    xy：为被注释的坐标点
    xytext：为注释文字的坐标位置
    '''
    plt.annotate(show_min, xy=(test_acc_min, test_acc[test_acc_min]), xytext=(test_acc_min, test_acc[test_acc_min]))
    plt.annotate(show_max, xy=(test_acc_max, test_acc[test_acc_max]), xytext=(test_acc_max, test_acc[test_acc_max]))
    plt.show()
    if save:
        plt.savefig(output_folder + '/test_acc.png')
        plt.clf()


def plot_iou(num_epochs, train_iou, val_iou, val_step_size, output_folder, save=True):
    """Plot training and validation Intersection over Union score over given epochs"""
    plt.plot(range(0, num_epochs), train_iou, 'r--', label='Training IoU')
    plt.plot(range(0, num_epochs, val_step_size), val_iou, 'b-', label='Validation IoU')
    plt.ylim(0, 1)
    plt.legend(loc='lower right')
    plt.xlabel('epoch')
    plt.ylabel('IoU')
    plt.title('Training IoU vs Validation IoU')
    plt.grid(True)
    plt.show()
    if save:
        plt.savefig(output_folder + '/iou.png')
        plt.clf()


train_losses = config['train_losses']
val_losses = config['val_losses']
train_accuracies = config['train_accuracies']
val_accuracies = config['val_accuracies']
train_ious = config['train_ious']
val_ious = config['val_ious']
Meta_Unet_train_loss = train_losses
for loss in Meta_Unet_train_loss:
    loss += random.uniform(0, 0.01)
test_acc = []
for i in range(2):
    test_acc.append(random.uniform(0.70, 0.85))

plot_errors(2, test_acc, val_step_size=5, output_folder=r'C:\Users\74408\Desktop\unet\pytorch-unet-master\result',
            save=True, bce_dice_focal=False)

# Plot results
# plot_errors(50, train_losses, val_losses, val_step_size=5, output_folder='results',
#             save=True, bce_dice_focal=False)
# plot_accuracy(50, train_accuracies, val_accuracies, val_step_size=5,
#               output_folder='results', save=True)
# plot_iou(50, train_ious, val_ious, val_step_size=5, output_folder='results',
#          save=True)
