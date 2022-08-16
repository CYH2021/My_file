# coding = utf-8

from os import system
import tkinter as tk
from webbrowser import open as web_open


# 清华大学镜像站 https://pypi.tuna.tsinghua.edu.cn/simple
# 中国科学技术大学镜像站 : https://pypi.mirrors.ustc.edu.cn/simple
# 豆瓣镜像站：http://pypi.douban.com/simple/
# 阿里云镜像站：http://mirrors.aliyun.com/pypi/simple/

class PIP:
    def __init__(self):
        print("\n\n请勿关闭此窗口,否则脚本无法运行\n\n")
        # 窗口设定
        self.win = tk.Tk()
        self.win.geometry("320x290+620+400")
        self.win.title("镜像站安装PY模块 GUI")
        self.win.resizable(False, False)

        # 提示
        tk.Label(self.win, text="请输入模块名或库名").pack(pady=15)

        # 输入模块名称与模块版本
        ents = tk.Frame(self.win)
        self.mk_name = tk.Entry(ents, width=15)
        self.mk_version = tk.Entry(ents, width=5)
        tk.Label(ents, text="模块名").pack(side=tk.LEFT)
        self.mk_name.pack(pady=10, side=tk.LEFT)
        tk.Label(ents, text="模块版本").pack(side=tk.LEFT)
        self.mk_version.pack(pady=10, side=tk.LEFT)
        ents.pack()
        tk.Label(text="不输入模块版本默认为模块的最新版本").pack()

        # 按钮区域
        command1 = tk.Frame(self.win)
        tk.Button(command1, text="安装", command=self.install).pack(ipadx=16, side=tk.LEFT)
        tk.Button(command1, text="卸载", command=self.uninstall).pack(ipadx=16, side=tk.LEFT)
        tk.Button(command1, text="升级", command=self.upgrade).pack(ipadx=16, side=tk.LEFT)
        tk.Button(command1, text="查看", command=self.show).pack(ipadx=16, side=tk.LEFT)
        command1.pack(side=tk.TOP)

        command2 = tk.Frame(self.win)
        tk.Button(command2, text="查看已安装的包", command=self.install_list).pack(ipadx=20, side=tk.LEFT)
        tk.Button(command2, text="查看可升级的包", command=self.upgrade_list).pack(ipadx=20, side=tk.LEFT)
        command2.pack(side=tk.TOP)

        tk.Button(self.win, text="清除命令行输出", command=self.cls).pack(ipadx=20)
        # 消息控件
        self.msg = tk.Label(self.win, text="", foreground="Red")
        self.msg.pack(ipady=6)

        # 镜像源
        tk.Label(text="镜像来源").pack()
        mirror_station = tk.Frame(self.win)
        link1 = tk.Label(mirror_station, text="清华镜像站", foreground="blue")
        link1.pack(side=tk.LEFT)
        link2 = tk.Label(mirror_station, text="北外镜像站", foreground="blue")
        link2.pack(side=tk.LEFT)
        link3 = tk.Label(mirror_station, text="豆瓣镜像站", foreground="blue")
        link3.pack(side=tk.LEFT)
        link4 = tk.Label(mirror_station, text="阿里云镜像站", foreground="blue")
        link4.pack(side=tk.LEFT)

        mirror_station.pack(fill=tk.X, padx=20)

        # 事件绑定
        link1.bind("<Button-1>", self.web_link_tuna_tsinghua)
        link2.bind("<Button-1>", self.web_link_mirrors_ustc)
        link3.bind("<Button-1>", self.web_link_tuna_douban)
        link4.bind("<Button-1>", self.web_link_mirrors_aliyun)
        self.win.mainloop()

    def install(self) -> None:
        mk = self.mk_name.get() + " " + self.mk_version.get()
        if mk == " ":
            print("请输入要安装的模块名或库名")
            self.msg.config(text="请输入要安装的模块名或库名")
            return None
        self.msg.config(text='安装中...')
        self.win.update()
        print("——" * 10 + "Installing 开始安装" + "——" * 10 + "\n")
        print("正在安装", mk)
        system("python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip")
        system(f"pip --default-timeout=100 install {mk} -i https://pypi.tuna.tsinghua.edu.cn/simple ")
        system(f"pip --default-timeout=100 install {mk} -i https://pypi.mirrors.ustc.edu.cn/simple ")
        system(f"pip --default-timeout=100 install {mk} -i http://pypi.douban.com/simple/ ")
        system(f"pip --default-timeout=100 install {mk} -i http://mirrors.aliyun.com/pypi/simple/ ")
        system(f"pip --default-timeout=500 install {mk}")
        print("\n" + "——" * 10 + "Install-over 安装结束" + "——" * 10)
        self.msg.config(text='安装结束')
        return None

    def uninstall(self) -> None:
        mk = self.mk_name.get()
        if mk == "":
            print("请输入要卸载的模块名或库名")
            self.msg.config(text="请输入要卸载的模块名或库名")
            return None
        self.msg.config(text='卸载中...')
        self.win.update()
        print("——" * 10 + "Uninstalling 开始卸载" + "——" * 10 + "\n")
        print("正在卸载", mk)
        system(f"pip uninstall -y {mk}")
        print("\n" + "——" * 10 + "Uninstall-over 卸载结束" + "——" * 10)
        self.msg.config(text='卸载结束')
        return None

    def upgrade(self) -> None:
        mk = self.mk_name.get() + " " + self.mk_version.get()
        if mk == " ":
            print("请输入要升级的模块名或库名")
            self.msg.config(text="请输入要升级的模块名或库名")
            return None
        self.msg.config(text='升级中...')
        self.win.update()
        print("——" * 10 + "开始升级" + "——" * 10 + "\n")
        print("正在升级", mk)
        system(f"pip install --upgrade {mk}")
        print("\n" + "——" * 10 + "升级结束" + "——" * 10)
        self.msg.config(text='升级结束')
        return None

    def show(self) -> None:
        mk = self.mk_name.get()
        if mk == "":
            print("请输入要查看的模块名或库名")
            self.msg.config(text="请输入要查看的模块名或库名")
            return None
        self.msg.config(text='加载中...')
        self.win.update()
        system("CLS")
        print("——" * 10 + f"{mk}信息" + "——" * 10 + "\n")
        system(f"pip show -f {mk}")
        print("\n" + "——" * 10 + "END" + "——" * 10)
        self.msg.config(text='请在命令行查看信息')
        return None

    def install_list(self) -> None:
        self.msg.config(text='加载中...')
        self.win.update()
        system("CLS")
        print("——" * 10 + f"已安装的包" + "——" * 10 + "\n")
        system(f"pip list")
        print("\n" + "——" * 10 + "END" + "——" * 10)
        self.msg.config(text='请在命令行查看信息')
        return None

    def upgrade_list(self) -> None:
        self.msg.config(text='加载中...')
        self.win.update()
        system("CLS")
        print("——" * 10 + f"可升级的包" + "——" * 10 + "\n")
        system(f"pip list -o")
        print("\n" + "——" * 10 + "END" + "——" * 10)
        self.msg.config(text='请在命令行查看信息')
        return None

    def cls(self) -> None:
        self.win.update()
        system("CLS")
        self.msg.config(text='已清除命令行输出')
        return None

    # bind:
    @staticmethod
    def web_link_tuna_tsinghua(event):
        web_open("https://mirrors.tuna.tsinghua.edu.cn/help/pypi/")

    @staticmethod
    def web_link_mirrors_ustc(event):
        web_open("https://mirrors.bfsu.edu.cn/pypi/web/")

    @staticmethod
    def web_link_tuna_douban(event):
        web_open("https://www.douban.com/")

    @staticmethod
    def web_link_mirrors_aliyun(event):
        web_open("https://developer.aliyun.com/mirror/")


PIP = PIP()  # 单窗口
