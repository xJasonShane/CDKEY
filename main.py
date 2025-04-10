import tkinter as tk
from tkinter import ttk
from generate_tab import GenerateTab
from verify_tab import VerifyTab
from about_tab import AboutTab

class CDKEYApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CDKEY生成与校验工具")
        
        # 创建主框架
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 创建标签页
        self.notebook = ttk.Notebook(self.main_frame)
        
        # 创建三个页面
        self.generate_tab = ttk.Frame(self.notebook)
        self.verify_tab = ttk.Frame(self.notebook)
        self.about_tab = ttk.Frame(self.notebook)
        
        # 添加标签页
        self.notebook.add(self.generate_tab, text="CDK生成")
        self.notebook.add(self.verify_tab, text="CDK校验")
        self.notebook.add(self.about_tab, text="关于")
        
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # 初始化各页面
        self.init_generate_tab()
        self.init_verify_tab()
        self.init_about_tab()
    
    def init_generate_tab(self):
        """初始化生成页面"""
        GenerateTab(self.generate_tab)
    
    def init_verify_tab(self):
        """初始化校验页面"""
        VerifyTab(self.verify_tab)
    
    def init_about_tab(self):
        """初始化关于页面"""
        AboutTab(self.about_tab)

if __name__ == "__main__":
    root = tk.Tk()
    app = CDKEYApp(root)
    root.mainloop()