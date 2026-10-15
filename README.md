# 图片格式转换工具

这是一个简单易用的图片格式转换工具，支持批量转换图片格式。

## 功能特点

- 支持批量选择图片文件
- 支持多种图片格式转换（PNG、JPEG、BMP、GIF、TIFF、WebP）
- 可自定义输出目录
- 图形界面操作，简单直观
- 运行时跨平台（PyQt6 + Pillow，Windows / macOS / Linux）

## 安装说明

1. 确保已安装 Python 3.8 或更高版本
2. 安装依赖包：
   ```bash
   pip install -r requirements.txt
   ```

## 使用方法

1. 运行程序：
   ```bash
   python image_converter.py
   ```
2. 点击"选择图片文件"按钮选择要转换的图片
3. 选择输出目录
4. 从下拉菜单选择目标格式
5. 如需在转换后删除原始文件，勾选"转换后删除源文件"（**会直接删除源文件，请先备份**）
6. 点击"开始转换"按钮进行转换

## 支持的格式

- PNG (.png)
- JPEG (.jpg)
- BMP (.bmp)
- GIF (.gif)
- TIFF (.tiff)
- WebP (.webp)

格式列表与 `image_converter.py` 中 `self.supported_formats` 一致；由 Pillow 实际写入，Pillow 不支持的写入方式会报错并在弹窗中提示。

## 打包为 exe（Windows）

仓库内提供 PyInstaller 配置：

- `build.py` — 调用 PyInstaller，使用 `--onefile --windowed --icon=icon.ico`，产物在 `dist/图片格式转换工具.exe`，并复制到 `release/`。
- `图片格式转换工具.spec` — 等价的 PyInstaller spec，`datas=[('icon.ico', '.')]`，主脚本 `image_converter.py`，图标 `icon.ico`（两者均已入库）。

```bash
pip install pyinstaller
python build.py
# 或
pyinstaller 图片格式转换工具.spec
```

注意：`build.py` 中 `--add-data=icon.ico;.` 使用 Windows 的分号分隔符，因此打包脚本本身仅在 Windows 下直接可用；在 macOS/Linux 上需把分号改为冒号。

`icon.py` 是图标生成脚本（Pillow 绘制），运行后会重新生成 `icon.ico` 与 `icon.png`；这两个图标文件已随仓库提交，无需重新生成。

## 注意事项

- 转换过程中请勿关闭程序
- 确保有足够的磁盘空间
- 建议在转换前备份原始图片；勾选"转换后删除源文件"会直接删除源文件，不可恢复

## License & Attribution / 许可与来源

Original project code authored for this repository is released under the MIT License; see [LICENSE](./LICENSE).

When reusing or redistributing a substantial portion, retain the LICENSE and its copyright notice. The copyright notice includes this original source URL: https://github.com/change979666/image-format-converter. Please keep the source link visible in your redistributed source or project documentation.

This license applies only to original material that the repository maintainer has the right to license. Third-party libraries, vendor code, platform SDKs, trademarks, screenshots, icons, fonts, and other external assets remain subject to their respective licenses and terms. Review those terms before reuse.

**Project status:** personal/archived project, shared as-is. Maintenance, compatibility, and production readiness are not guaranteed.
