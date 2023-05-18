import os

from torch.utils.data import Dataset
from utils import *
from torchvision import transforms
transform=transforms.Compose([
    transforms.ToTensor()
])

class MyDataset(Dataset):
    def __init__(self,path):
        self.path=path
        self.name=os.listdir(os.path.join(path,'SegmentationClass'))

    def __len__(self):
        return len(self.name)

    def __getitem__(self, index):
        segment_name=self.name[index]  #xx.png
        segment_path=os.path.join(self.path,'SegmentationClass',segment_name)#标签地址
        image_path=os.path.join(self.path,'JPEGImages',segment_name.replace('png','jpg'))#原图地址
        segment_image=keep_image_size_open(segment_path)#读取图片，等比缩放，网络需要尺寸大小一样的图片作为输入
        image=keep_image_size_open(image_path)
        return transform(image),transform(segment_image)#归一化

if __name__ == '__main__':
    data=MyDataset(r'C:\Users\74408\Desktop\unet\pytorch-unet-master\data')
    print(data[0][0].shape)
    print(data[0][1].shape)