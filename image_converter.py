#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
图片格式转换工具
支持批量转换图片格式，提供图形界面操作
"""

import sys
import os
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, 
                           QVBoxLayout, QHBoxLayout, QWidget, QFileDialog, 
                           QComboBox, QLineEdit, QMessageBox, QListWidget,
                           QCheckBox, QFrame)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
from PIL import Image

# 获取资源路径
def resource_path(relative_path):
    """获取资源的绝对路径"""
    try:
        # PyInstaller创建临时文件夹，将路径存储在_MEIPASS中
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

class ImageConverter(QMainWindow):
    """
    图片格式转换器主窗口类
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle("图片格式转换工具")
        self.setMinimumSize(800, 600)
        
        # 设置窗口图标
        icon_path = resource_path("icon.ico")
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        
        # 支持的图片格式
        self.supported_formats = {
            "PNG": ".png",
            "JPEG": ".jpg",
            "BMP": ".bmp",
            "GIF": ".gif",
            "TIFF": ".tiff",
            "WebP": ".webp"
        }
        
        self.init_ui()
        
    def init_ui(self):
        """
        初始化用户界面
        """
        # 创建主窗口部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建主布局
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # 创建标题标签
        title_label = QLabel("图片格式转换工具")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title_label.setFont(title_font)
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # 创建选择文件按钮
        select_button = QPushButton("选择图片文件")
        select_button.setMinimumHeight(40)
        select_button.setFont(QFont("Microsoft YaHei", 10))
        select_button.clicked.connect(self.select_files)
        
        # 创建文件列表显示
        self.file_list = QListWidget()
        self.file_list.setFont(QFont("Microsoft YaHei", 10))
        self.file_list.setMinimumHeight(200)
        
        # 创建底部控制面板
        control_panel = QFrame()
        control_panel.setFrameStyle(QFrame.Shape.StyledPanel)
        control_layout = QVBoxLayout(control_panel)
        control_layout.setSpacing(15)
        
        # 创建输出目录选择
        output_layout = QHBoxLayout()
        output_label = QLabel("输出目录:")
        output_label.setFont(QFont("Microsoft YaHei", 10))
        self.output_path = QLineEdit()
        self.output_path.setFont(QFont("Microsoft YaHei", 10))
        output_button = QPushButton("浏览")
        output_button.setFont(QFont("Microsoft YaHei", 10))
        output_button.clicked.connect(self.select_output_dir)
        output_layout.addWidget(output_label)
        output_layout.addWidget(self.output_path)
        output_layout.addWidget(output_button)
        
        # 创建格式选择和删除选项的布局
        options_layout = QHBoxLayout()
        
        # 创建格式选择下拉框
        format_label = QLabel("目标格式:")
        format_label.setFont(QFont("Microsoft YaHei", 10))
        self.format_combo = QComboBox()
        self.format_combo.setFont(QFont("Microsoft YaHei", 10))
        self.format_combo.addItems(self.supported_formats.keys())
        self.format_combo.setMinimumWidth(150)
        
        # 创建删除源文件复选框
        self.delete_source_checkbox = QCheckBox("转换后删除源文件")
        self.delete_source_checkbox.setFont(QFont("Microsoft YaHei", 10))
        self.delete_source_checkbox.setToolTip("转换完成后删除原始图片文件")
        
        options_layout.addWidget(format_label)
        options_layout.addWidget(self.format_combo)
        options_layout.addWidget(self.delete_source_checkbox)
        options_layout.addStretch()
        
        # 创建转换按钮
        convert_button = QPushButton("开始转换")
        convert_button.setMinimumHeight(50)
        convert_button.setFont(QFont("Microsoft YaHei", 12, QFont.Weight.Bold))
        convert_button.clicked.connect(self.convert_images)
        
        # 添加所有部件到控制面板布局
        control_layout.addLayout(output_layout)
        control_layout.addLayout(options_layout)
        control_layout.addWidget(convert_button)
        
        # 添加所有部件到主布局
        main_layout.addWidget(title_label)
        main_layout.addWidget(select_button)
        main_layout.addWidget(self.file_list)
        main_layout.addWidget(control_panel)
        
    def select_files(self):
        """
        选择要转换的图片文件
        """
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "选择图片文件",
            "",
            "图片文件 (*.png *.jpg *.jpeg *.bmp *.gif *.tiff *.webp)"
        )
        if files:
            self.file_list.clear()
            self.file_list.addItems(files)
            
    def select_output_dir(self):
        """
        选择输出目录
        """
        directory = QFileDialog.getExistingDirectory(
            self,
            "选择输出目录"
        )
        if directory:
            self.output_path.setText(directory)
            
    def convert_images(self):
        """
        转换图片格式
        """
        if not self.file_list.count():
            QMessageBox.warning(self, "警告", "请先选择要转换的图片文件！")
            return
            
        output_dir = self.output_path.text()
        if not output_dir:
            QMessageBox.warning(self, "警告", "请选择输出目录！")
            return
            
        target_format = self.format_combo.currentText()
        extension = self.supported_formats[target_format]
        
        success_count = 0
        delete_count = 0
        
        for i in range(self.file_list.count()):
            input_path = self.file_list.item(i).text()
            try:
                # 打开图片
                with Image.open(input_path) as img:
                    # 获取文件名（不含扩展名）
                    filename = os.path.splitext(os.path.basename(input_path))[0]
                    # 构建输出路径
                    output_path = os.path.join(output_dir, filename + extension)
                    # 保存图片
                    img.save(output_path, target_format)
                success_count += 1
                
                # 如果选中了删除源文件选项，则删除原始文件
                if self.delete_source_checkbox.isChecked():
                    try:
                        os.remove(input_path)
                        delete_count += 1
                    except Exception as e:
                        QMessageBox.warning(self, "警告", f"删除源文件 {input_path} 时出错：{str(e)}")
                        
            except Exception as e:
                QMessageBox.warning(self, "错误", f"转换文件 {input_path} 时出错：{str(e)}")
        
        # 显示转换结果
        result_message = f"成功转换 {success_count} 个文件！"
        if self.delete_source_checkbox.isChecked():
            result_message += f"\n成功删除 {delete_count} 个源文件！"
        QMessageBox.information(self, "完成", result_message)

def main():
    """
    程序入口函数
    """
    app = QApplication(sys.argv)
    window = ImageConverter()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main() 