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
        ttk.Label(self.about_frame, text="CDKEY生成与校验工具", font=('Arial', 14, 'bold')).pack(pady=10)
        
        info_frame = ttk.Frame(self.about_frame)
        info_frame.pack(pady=5)
        
        ttk.Label(info_frame, text="版本: 1.0.0").grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        ttk.Label(info_frame, text="作者: ").grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        ttk.Label(info_frame, text="GitHub: ").grid(row=2, column=0, sticky=tk.W, padx=5, pady=2)
        
        # 作者信息
        ttk.Label(info_frame, text="示例作者").grid(row=1, column=1, sticky=tk.W, padx=5, pady=2)
        github_link = ttk.Label(info_frame, text="https://github.com/example", foreground="blue", cursor="hand2")
        github_link.grid(row=2, column=1, sticky=tk.W, padx=5, pady=2)
        github_link.bind("<Button-1>", lambda e: self.open_github())
        
        # 版权信息
        ttk.Label(self.about_frame, text="© 2023 版权所有").pack(pady=10)
    
    def open_github(self):
        """打开GitHub链接"""
        import webbrowser
        webbrowser.open("https://github.com/example")