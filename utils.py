from PIL import Image


def keep_image_size_open(path, size=(256, 256)):
    img = Image.open(path)#取图片
    temp = max(img.size)#最长边
    mask = Image.new('RGB', (temp, temp), (0, 0, 0))
    mask.paste(img, (0, 0))
    mask = mask.resize(size)
    return mask
def keep_image_size_read(pic, size=(256, 256)):
    # img = Image.open(pic)#取图片
    temp = max(pic.size)#最长边
    mask = Image.new('RGB', (temp, temp), (0, 0, 0))
    mask.paste(pic, (0, 0))
    mask = mask.resize(size)
    return mask