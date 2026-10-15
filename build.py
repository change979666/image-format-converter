#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
打包脚本，用于生成可执行文件
"""

import os
import subprocess
import sys
import shutil

def build_exe():
    """
    使用PyInstaller打包程序
    """
    print("开始打包程序...")
    
    # 确保图标文件存在
    if not os.path.exists('icon.ico'):
        print("错误: 找不到图标文件 icon.ico")
        return
    
    # 构建PyInstaller命令
    cmd = [
        'pyinstaller',
        '--name=图片格式转换工具',
        '--windowed',  # 不显示控制台窗口
        '--onefile',   # 打包成单个文件
        '--icon=icon.ico',  # 设置图标
        '--clean',     # 清理临时文件
        '--add-data=icon.ico;.',  # 添加图标文件到打包中
        'image_converter.py'  # 主程序文件
    ]
    
    # 执行打包命令
    subprocess.call(cmd)
    
    print("打包完成！")
    print("可执行文件位于: dist/图片格式转换工具.exe")
    
    # 创建发布文件夹
    if not os.path.exists('release'):
        os.makedirs('release')
    
    # 复制可执行文件到发布文件夹
    shutil.copy('dist/图片格式转换工具.exe', 'release/图片格式转换工具.exe')
    
    # 复制README文件到发布文件夹
    if os.path.exists('README.md'):
        shutil.copy('README.md', 'release/README.md')
    
    print("发布文件已复制到 release 文件夹")

if __name__ == "__main__":
    build_exe() 