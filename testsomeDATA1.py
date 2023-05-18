import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score
from torch import optim
from torch.utils.data import DataLoader
from torchvision.utils import save_image

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
    y_true_list = []
    y_pred_list = []
    y_scores_list = []
    iou_list=[]
    acc_list=[]
    loss_list=[]
    while True:
        for i, (image, segment_image) in enumerate(data_loader):
            image, segment_image = image.to(device), segment_image.to(device)
            out_image = net(image)
            train_loss = loss_fun(out_image, segment_image)
            opt.zero_grad()
            train_loss.backward()
            opt.step()

            print(f'{epoch}-{i}-train_loss===>>{train_loss.item()}')
            print('Epoch [{}/{}], Step [{}/{}], Loss: {:.4f}'.format(epoch + 1, epoch, i + 1, len(data_loader),
                                                                     train_loss.item()))

            _image = image[0]
            _segment_image = segment_image[0]
            _out_image = out_image[0]
            img = torch.stack([_image, _segment_image, out_image[0]], dim=0)
            save_image(img, f'{save_path}/{i}.png')

            y_true = _segment_image.detach().cpu().numpy().flatten()
            y_true = np.where(y_true > 0.5, 1, 0)
            y_pred = (_out_image.detach().cpu().numpy().flatten() > 0.5).astype(int)
            y_pred = np.where(y_pred > 0.5, 1, 0)
            y_scores = _out_image.detach().cpu().numpy().flatten()
            y_scores = (y_scores - y_scores.min()) / (y_scores.max() - y_scores.min())
            # 计算IOU和ACC

            # 保存loss
            loss_list.append(train_loss.item())

            y_true_list.extend(y_true)
            y_pred_list.extend(y_pred)
            y_scores_list.extend(y_scores)

            tn, fp, fn, tp = confusion_matrix(y_true_list, y_pred_list).ravel()
            iou = tp / (tp + fp + fn)
            acc = accuracy_score(y_true_list, y_pred_list)
            # 保存acc和iou
            iou_list.append(np.array([iou]))
            acc_list.append(np.array([acc]))
            # 打印IOU和ACC
            print(f'IOU: {iou:.4f}')
            print(f'ACC: {acc:.4f}')
            if i==50 :
                break
        epoch += 1
        break

    # 保存 y_true y_pred y_scores 到txt
    np.savetxt('y_true.txt', y_true_list)
    np.savetxt('y_pred.txt', y_pred_list)
    np.savetxt('y_scores.txt', y_scores_list)
    np.savetxt('acc.txt', acc_list)
    np.savetxt('iou.txt', iou_list)
    np.savetxt('loss_list.txt', loss_list)


