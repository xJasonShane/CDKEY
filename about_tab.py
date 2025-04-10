import tkinter as tk
from tkinter import ttk

class AboutTab:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()
    
    def setup_ui(self):
        """设置关于页面UI"""
        self.about_frame = ttk.LabelFrame(self.parent, text="关于")
        self.about_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # 软件信息
        self.app_info = {
            "version": "α 1.0",
            "author": "JasonShane",
            "github": "https://github.com/example",
            "update_date": "2025-04-10"
        }
        
        info_frame = ttk.Frame(self.about_frame, padding=10)
        info_frame.pack(padx=10, pady=10)
        
        ttk.Label(info_frame, text=f"版本: {self.app_info['version']}").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        ttk.Label(info_frame, text=f"作者: {self.app_info['author']}").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        github_link = ttk.Label(info_frame, text=f"GitHub: {self.app_info['github']}", foreground="blue", cursor="hand2")
        github_link.grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        ttk.Label(info_frame, text=f"更新日期: {self.app_info['update_date']}").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        github_link.bind("<Button-1>", lambda e: self.open_github())
    
    def open_github(self):
        """打开GitHub链接"""
        import webbrowser
        webbrowser.open(self.app_info['github'])