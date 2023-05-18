import os

import matplotlib.pyplot as plt
import numpy as np
import torch
from click.core import batch
from sklearn.metrics import accuracy_score

from net import *
from utils import keep_image_size_open
from data import *
from torchvision.utils import save_image
def test():
    net=UNet().cpu()#
#------------写成函数被其他py调用时一定要用绝对地址--------------
    weights=r'C:\Users\74408\Desktop\unet\pytorch-unet-master\params/unet.pth'

    if os.path.exists(weights):
        net.load_state_dict(torch.load(weights))
        print('successfully')
    else:
        print('no loading')


    _input=input('please input JPEGImages path:')
    # _input=r'C:\Users\74408\Desktop\unet\pytorch-unet-master\data\JPEGImages\39.jpg'
    img=keep_image_size_open(_input)
    img_data=transform(img).cpu()
    print(img_data.shape)
    img_data=torch.unsqueeze(img_data,dim=0)
    out=net(img_data)

    save_image(out,r'C:\Users\74408\Desktop\unet\pytorch-unet-master\result/result.gif')

test()