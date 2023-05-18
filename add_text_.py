import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import time

# -*- coding: utf-8 -*-

def add_text(img):
    if img is None:
        print("getloss!")
    else:
        # bk_img = cv2.imread(ing)
        bk_img = img
        fontpath = "font/simsun.ttc"
        font = ImageFont.truetype(fontpath, 18)
        img_pil = Image.fromarray(bk_img)
        draw = ImageDraw.Draw(img_pil)
        timestr=time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))  #格式化时间
        fillcolor = '#00ff00'   #RGB红色
        #绘制文字信息
        draw.text((10, 10), timestr+'     00', font=font, fill=fillcolor)

        bk_img = np.array(img_pil)
        cv2.imshow("add_text",bk_img)
        cv2.waitKey()
        cv2.imwrite("add_text.jpg",bk_img)
        # save_image(img, f'{save_path}/{i}.png')
        return  bk_img

def getTime():
    timestr = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime(time.time()))  # 格式化时间
    return timestr

if __name__ == '__main__':

    it=str(1)+getTime()
    print(it)
    img = cv2.imread("train_image/0.png")
    # add_text(img)

    # if img is None:
    #     print("getloss!")
    # else:add_text(img)





