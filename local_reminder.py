#!/usr/bin/env python3
import time
import datetime
import schedule
import sys
import tkinter as tk
from tkinter import messagebox
import threading

# 目标日期：2025年5月15日
TARGET_DATE = datetime.datetime(2025, 5, 15)

def calculate_days_remaining():
    """
    计算当前日期到目标日期的剩余天数。
    """
    now = datetime.datetime.now()
    # 仅比较日期部分，保证每天精确提醒一次
    remaining = TARGET_DATE.date() - now.date()
    return remaining.days

def show_reminder_window():
    """
    显示本地弹窗提醒
    """
    days = calculate_days_remaining()
    if days >= 0:
        message = f"距离2025年5月15日还有 {days} 天"
    else:
        message = f"距离2025年5月15日已经过去 {-days} 天"
    
    # 创建一个隐藏的主窗口
    root = tk.Tk()
    root.withdraw()
    
    # 设置窗口始终在最前面
    root.attributes('-topmost', True)
    
    # 显示消息框
    messagebox.showinfo("投稿倒计时提醒", message)
    
    # 关闭主窗口    
    root.destroy()
    
    # 打印到控制台
    print(f"【提醒】{message}")

def show_reminder_window_threaded():
    """
    在新线程中显示提醒窗口，避免阻塞主线程
    """
    thread = threading.Thread(target=show_reminder_window)
    thread.daemon = True
    thread.start()

def main():
    # 程序启动时立即提醒一次
    show_reminder_window()
    
    # 安排每天在09:00执行一次提醒
    schedule.every().day.at("09:30").do(show_reminder_window_threaded)
    
    print("本地提醒程序已启动（按 Ctrl+C 退出）")
    
    # 循环运行，等待定时任务执行
    try:
        while True:
            schedule.run_pending()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n程序已手动关闭")
        sys.exit(0)

if __name__ == "__main__":
    main()