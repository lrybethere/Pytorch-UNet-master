import numpy as np
from torch import optim
from torch.utils.data import DataLoader
from torchvision.utils import save_image
from sklearn.metrics import roc_curve, auc

from data import *
from net import *

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
weight_path = 'params/unet.pth'
data_path = r'data'
save_path = 'test_image'

if __name__ == '__main__':
    data_loader = DataLoader(MyDataset(data_path), batch_size=2, shuffle=True)
    net = UNet().to(device)
    if os.path.exists(weight_path):
        net.load_state_dict(torch.load(weight_path))
        print('successful load weight！')
    else:
        print('not successful load weight')

    lr = 1e-4
    opt = optim.Adam(net.parameters(), lr=lr)
    loss_fun = nn.BCELoss()

    epoch = 1
    while True:
        for i, (image, segment_image) in enumerate(data_loader):
            image, segment_image = image.to(device), segment_image.to(device)
            out_image = net(image)
            train_loss = loss_fun(out_image, segment_image)
            opt.zero_grad()
            train_loss.backward()
            opt.step()

            # loss
            print(f'{epoch}-{i}-train_loss===>>{train_loss.item()}')

            _image = image[0]
            _segment_image = segment_image[0]
            _out_image = out_image[0]
            img = torch.stack([_image, _segment_image, out_image[0]], dim=0)
            save_image(img, f'{save_path}/{i}.png')

        epoch += 1
        torch.cuda.empty_cache()
    #保存y_true、y_pred,y_scores到txt
