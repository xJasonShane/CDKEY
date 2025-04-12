import tkinter as tk
from tkinter import ttk
import os

class AboutTab:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()
    
    def setup_ui(self):
        """设置关于页面UI"""
        self.about_frame = ttk.LabelFrame(self.parent, text="关于")
        self.about_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 软件信息
        # 从update.txt获取更新日期
        update_date = self.get_update_date()
        self.app_info = {
            "version": "α 1.1",
            "author": "JasonShane",
            "github": "https://github.com/xJasonShane/CDKEY",
            "update_date": update_date
        }
        
        info_frame = ttk.Frame(self.about_frame, padding=(10, 10, 10, 10))
        info_frame.pack(padx=10, pady=10)
        
        ttk.Label(info_frame, text=f"版本: {self.app_info['version']}").grid(row=0, column=0, sticky=tk.W, padx=10, pady=10)
        ttk.Label(info_frame, text=f"作者: {self.app_info['author']}").grid(row=1, column=0, sticky=tk.W, padx=10, pady=10)
        ttk.Label(info_frame, text="GitHub:").grid(row=2, column=0, sticky=tk.W, padx=10, pady=10)
        github_link = ttk.Label(info_frame, text=self.app_info['github'], foreground="blue", cursor="hand2")
        github_link.grid(row=2, column=1, sticky=tk.W, pady=10)
        ttk.Label(info_frame, text="更新日期:").grid(row=3, column=0, sticky=tk.W, padx=10, pady=10)
        update_link = ttk.Label(info_frame, text=self.app_info['update_date'], foreground="blue", cursor="hand2")
        update_link.grid(row=3, column=1, sticky=tk.W, pady=10)
        update_link.bind("<Button-1>", lambda e: self.open_update_file())
        github_link.bind("<Button-1>", lambda e: self.open_github())
    
    def open_github(self):
        """打开GitHub链接"""
        import webbrowser
        webbrowser.open(self.app_info['github'])
        
    def get_update_date(self):
        """从update.txt获取更新日期"""
        try:
            with open("update.txt", "r", encoding="utf-8") as f:
                first_line = f.readline().strip()
                # 从第一行提取日期部分
                parts = first_line.split()
                if len(parts) >= 3:
                    return parts[2]
        except Exception:
            pass
        return "2025-04-10"  # 默认日期
        
    def open_update_file(self):
        """打开update.txt文件"""
        os.startfile("update.txt")