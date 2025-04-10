import tkinter as tk
from tkinter import ttk, messagebox

class VerifyTab:
    def __init__(self, parent):
        self.parent = parent
        self.setup_ui()
    
    def setup_ui(self):
        """设置校验页面UI"""
        # 校验面板
        self.verify_frame = ttk.LabelFrame(self.parent, text="CDK校验")
        self.verify_frame.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        # CDK输入
        ttk.Label(self.verify_frame, text="输入CDK:").pack(pady=5)
        self.cdkey_entry = ttk.Entry(self.verify_frame, width=40)
        self.cdkey_entry.pack(pady=5)
        
        # 校验按钮
        ttk.Button(self.verify_frame, text="校验", command=self.verify_cdkey).pack(pady=10)
        
        # 结果显示
        self.result_label = ttk.Label(self.verify_frame, text="")
        self.result_label.pack(pady=5)
    
    def verify_cdkey(self):
        """校验CDKEY"""
        cdkey = self.cdkey_entry.get().strip()
        if not cdkey:
            messagebox.showerror("错误", "请输入CDKEY")
            return
        
        # 这里可以添加实际的校验逻辑
        # 目前只是模拟校验
        if len(cdkey) >= 8 and any(c.isdigit() for c in cdkey) and any(c.isalpha() for c in cdkey):
            self.result_label.config(text="校验成功", foreground="green")
        else:
            self.result_label.config(text="校验失败", foreground="red")