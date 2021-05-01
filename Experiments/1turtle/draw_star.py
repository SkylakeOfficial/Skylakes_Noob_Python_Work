from turtle import *


def draw_star(scl=1, rot=0):
    begin_fill()
    left(36 - rot)
    for i in range(5):
        forward(scl * 100)
        left(144)
    end_fill()


def ask_color(factor_name, default_color_name='黑色', default_color=[0, 0, 0]):
    col = default_color
    select = input('要自定义{}吗？默认颜色为{}。\nY/N\n'.format(factor_name, default_color_name))
    if select == 'Y' or select == 'y':
        print('请分别输入R、G、B分量(0到255的整数，多余部分会被裁剪)')
        try:
            col = [int(input('R:')), int(input('G:')), int(input('B:'))]
            for i in range(3):
                if 0 > col[i]:
                    col[i] = 0
                elif col[i] > 255:
                    col[i] = 255
        except:
            print('非法字符!{}已重置为默认'.format(factor_name))
            col = default_color

    return col


# set geometric parameters
try:
    scale = int(input('请输入绘制五角星的大小，回车为默认\n'))
except:
    print('五角星大小为默认值1')
    scale = 1
try:
    rotation = int(input('请输入五角星的旋转角度，回车为默认\n'))
except:
    print('五角星旋转角度为默认值0')
    rotation = 0

# get color parameters
outline_color = ask_color('五角星轮廓色')
fill_color = ask_color('五角星填充颜色', '黄色', [255, 211, 88])
canvas_color = ask_color('画布的颜色', '灰色', [200, 200, 200])

print('开始绘制...')

# set colors
colormode(255)
fillcolor(fill_color[0], fill_color[1], fill_color[2])
pencolor(outline_color[0], outline_color[1], outline_color[2])
bgcolor(canvas_color[0], canvas_color[1], canvas_color[2])

# draw!
ht()
draw_star(scale, rotation)
done()
