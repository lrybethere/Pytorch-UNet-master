import os

from click.core import batch
from sklearn.metrics import accuracy_score

from add_text_ import *
from torch import nn,optim
import torch
from torch.utils.data import DataLoader
from data import *
from net import *
from torchvision.utils import save_image

losspic=[]
lossepoc=[]

device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')#设备
weight_path='params/unet.pth'
data_path=r'data'##这里输入训练图片路径
save_path='train_image'

# loss初值 +无穷
best_loss = float('inf')


if __name__ == '__main__':
    data_loader=DataLoader(MyDataset(data_path),batch_size=2,shuffle=True)
    net=UNet().to(device)
    if os.path.exists(weight_path):
        net.load_state_dict(torch.load(weight_path))
        print('successful load weight！')
    else:
        print('not successful load weight')

    # 优化函数adam
    lr=1e-4
    opt=optim.Adam(net.parameters(),lr=lr)
    loss_fun=nn.BCELoss()

    epoch=1
    while True:
        for i,(image,segment_image) in enumerate(data_loader):
            image, segment_image=image.to(device),segment_image.to(device)
            out_image=net(image)
            train_loss=loss_fun(out_image,segment_image)
            opt.zero_grad()
            train_loss.backward()
            opt.step()
            # print(len(data_loader))
            # print(i)
            losspic.append(train_loss.item())
            if i%10==0:#输出
                print(f'{epoch}-{i}-train_loss===>>{train_loss.item()}')
            # if i%50==0:#保存权重
            if train_loss.item() < best_loss:
                best_loss = train_loss.item()
                torch.save(net.state_dict(),weight_path)
                print("保存权重")
            if i%7==0:
                _image=image[0]
                _segment_image=segment_image[0]
                _out_image=out_image[0]
                img=torch.stack([_image,_segment_image,_out_image],dim=0)
                # it=str(i)+'_'+getTime()#降低效率，注释
                save_image(img,f'{save_path}/{i}.png')
        # 使用 sum() 函数计算数组的总和
        array_sum = sum(losspic)
        # 使用 len() 函数计算数组的长度
        array_len = len(losspic)
        # 计算数组的平均值
        array_mean = array_sum / array_len
        lossepoc.append(array_mean)
        # xunlainc
        # if epoch==10:break
        epoch+=1

# 将 loss 值保存到文本文件中
with open('loss_ecery_pic.txt', 'w') as f:
    for item in losspic:
        f.write(str(item) + '\n')
with open('loss_every_epoch.txt', 'w') as f:
    for item in lossepoc:
        f.write(str(item) + '\n')