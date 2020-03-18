#  这个是图形验证码
from .public_color import get_random_color
from .public_str import selected_chrs
from PIL import Image, ImageDraw, ImageFont
from random import choice, randint, randrange
from io import BytesIO
import os
import base64


def get_authcode_picture(size=(200, 100), chrNumber=6, bgcolor=(255, 255, 255)):
    """
    定义图片大小，验证码长度，背景颜色
    :param size:
    :param chrNumber:
    :param bgcolor:
    :return:
    """
    # 创建空白图像和绘图对象
    image_tmp = Image.new('RGB', size, bgcolor)
    draw = ImageDraw.Draw(image_tmp)

    # 生成并计算随机字符的宽度和高度
    text = selected_chrs(chrNumber)
    # 系统免费字体路径 /usr/share/fonts/truetype/freefont 也可以使用自定义的字体路径
    font = ImageFont.truetype('FreeMono.ttf', 48)  # 选定一款系统字体
    width, height = draw.textsize(text, font)
    if width + 2 * chrNumber > size[0] or height > size[1]:
        print('Size Error!')
        return

    # 绘制字符串
    startX = 0
    width_eachchr = width // chrNumber  # 计算每个字符宽度
    for i in range(chrNumber):
        startX += width_eachchr + 1
        position = (startX, (size[1] - height) // 2 + randint(-10, 10))  # 字符坐标, Y坐标上下浮动
        draw.text(xy=position, text=text[i], font=font, fill=get_random_color())  # 绘制函数

    # 对像素位置进行微调，实现验证码扭曲效果
    img_final = Image.new('RGB', size, bgcolor)
    pixels_final = img_final.load()
    pixels_tmp = image_tmp.load()
    for y in range(size[1]):
        offset = randint(-1, 0)  # randint()相当于闭区间[x,y]
        for x in range(size[0]):
            newx = x + offset  # 像素微调
            if newx >= size[0]:
                newx = size[0] - 1
            elif newx < 0:
                newx = 0
            pixels_final[newx, y] = pixels_tmp[x, y]

    # 绘制随机颜色随机位置的干扰像素
    draw = ImageDraw.Draw(img_final)
    for i in range(int(size[0] * size[1] * 0.07)):  # 7%密度的干扰像素
        draw.point((randrange(size[0]), randrange(size[1])), fill=get_random_color())  # randrange取值范围是左开右闭

    # 绘制随机干扰线，这里设置为8条
    for i in range(8):
        start = (0, randrange(size[1]))
        end = (size[0], randrange(size[1]))
        draw.line([start, end], fill=get_random_color(), width=1)

    # 绘制随机弧线
    for i in range(8):
        start = (-50, -50)  # 起始位置在外边看起来才会像弧线
        end = (size[0] + 10, randint(0, size[1] + 10))
        draw.arc(start + end, 0, 360, fill=get_random_color())

    # 创建buf 用来保存图片,在内存当中
    buf = BytesIO();
    img_final.save(buf,'png')

    # buf 图片数据,text 这个是图形验证码
    return (buf.getvalue(),text);

    #
    # img_final.save('Veri_code.png')
    # img_final.show()