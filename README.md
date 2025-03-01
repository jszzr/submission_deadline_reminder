# 论文投稿倒计时提醒器

一个简单的桌面应用程序，用于提醒论文截止日期，帮助你合理安排写作进度。

## 功能特点

- 每天自动在09:30弹出倒计时提醒
- 显示距离截止日期的剩余天数
- 置顶显示提醒窗口
- 支持控制台日志输出
- 后台运行，不影响其他工作

## 使用方法

1. 安装依赖：

```bash
pip install schedule
```

2. 运行程序：

```bash
python local_reminder.py
```

3. 程序会在后台运行，每天09:30自动弹出提醒窗口
4. 按Ctrl+C可以退出程序

## 自定义设置

- 默认截止日期为2025年5月15日
- 可以通过修改 `TARGET_DATE`变量更改目标日期
- 可以通过修改 `schedule.every().day.at()`参数更改提醒时间

## 依赖项

- Python 3.x
- schedule
- tkinter (Python标准库)

## 许可证

MIT License
