#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
生成程序图标
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_icon():
    """
    创建程序图标
    """
    # 创建一个512x512的图像，背景为白色
    img = Image.new('RGBA', (512, 512), (255, 255, 255, 0))
    draw = ImageDraw.Draw(img)
    
    # 绘制圆形背景
    draw.ellipse((50, 50, 462, 462), fill=(52, 152, 219))
    
    # 绘制内部圆形
    draw.ellipse((100, 100, 412, 412), fill=(41, 128, 185))
    
    # 绘制图片图标
    draw.rectangle((156, 156, 356, 356), fill=(255, 255, 255))
    
    # 绘制图片图标内部线条
    draw.line((206, 206, 306, 206), fill=(41, 128, 185), width=10)
    draw.line((206, 256, 306, 256), fill=(41, 128, 185), width=10)
    draw.line((206, 306, 306, 306), fill=(41, 128, 185), width=10)
    
    # 保存为ICO文件
    img.save('icon.ico', format='ICO')
    
    # 保存为PNG文件
    img.save('icon.png', format='PNG')
    
    print("图标已创建: icon.ico 和 icon.png")

if __name__ == "__main__":
    create_icon() 