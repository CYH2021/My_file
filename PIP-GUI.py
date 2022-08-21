# coding = utf-8

from os import system
import tkinter as tk
import tkinter.messagebox as mbox
from webbrowser import open as web_open
import asyncio
import time


# 清华大学镜像站 https://pypi.tuna.tsinghua.edu.cn/simple
# 中国科学技术大学镜像站 : https://pypi.mirrors.ustc.edu.cn/simple
# 豆瓣镜像站：http://pypi.douban.com/simple/
# 阿里云镜像站：http://mirrors.aliyun.com/pypi/simple/

class PIP:
    def __init__(self):
        print("\n\n请勿关闭此窗口,否则脚本无法运行\n\n")
        # 窗口设定
        self.win = tk.Tk()
        self.win.geometry("320x290+940+400")
        self.win.title("镜像站安装PY包 GUI")
        self.win.resizable(False, False)
        self.win.attributes("-topmost", True)

        # 提示
        tk.Label(self.win, text="请输入模块/包名").pack(pady=15)

        # 输入模块名称与模块版本
        ents = tk.Frame(self.win)
        self.mk_name = tk.Entry(ents, width=15)
        self.mk_version = tk.Entry(ents, width=5)
        tk.Label(ents, text="模块/包名").pack(side=tk.LEFT)
        self.mk_name.pack(pady=10, side=tk.LEFT)
        tk.Label(ents, text="版本").pack(side=tk.LEFT)
        self.mk_version.pack(pady=10, side=tk.LEFT)
        ents.pack()
        tk.Label(text="不输入版本默认为最新版本").pack()

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

        command3 = tk.Frame(self.win)
        tk.Button(command3, text="清除命令行输出", command=self.cls).pack(ipadx=20, side=tk.LEFT)
        tk.Button(command3, text="镜像站设为默认", command=self.default).pack(ipadx=20, side=tk.LEFT)

        command3.pack(side=tk.TOP)
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

    @staticmethod
    async def download(mk: str, mode: str = "install"):
        if mode == 'upgrade':
            mode = "install --upgrade"

        async def asyncio_download(mk_, mode_):
            system("python -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip")
            system(f"pip --default-timeout=100 {mode_} {mk_} -i https://pypi.tuna.tsinghua.edu.cn/simple ")
            system(f"pip --default-timeout=100 {mode_} {mk_} -i https://pypi.mirrors.ustc.edu.cn/simple ")
            system(f"pip --default-timeout=100 {mode_} {mk_} -i http://pypi.douban.com/simple/ ")
            system(f"pip --default-timeout=100 {mode_} {mk_} -i http://mirrors.aliyun.com/pypi/simple/ ")
            system(f"pip --default-timeout=500 {mode_} {mk_}")

        await asyncio_download(mk, mode)

    def install(self) -> None:
        mk = self.mk_name.get() + " " + self.mk_version.get()
        if mk == " ":
            print("请输入要安装的模块/包名")
            self.msg.config(text="请输入要安装的模块/包名")
            return None
        self.msg.config(text='安装中...')
        self.win.update()
        system("CLS")
        print("——" * 10 + "Installing 开始安装" + "——" * 10 + "\n")
        print("正在安装", mk)
        asyncio.run(PIP.download(mk, "install"))
        print("\n" + "——" * 10 + "Install-over 安装结束" + "——" * 10)
        self.msg.config(text='安装结束')
        return None

    def uninstall(self) -> None:
        mk = self.mk_name.get()
        if mk == "":
            print("请输入要卸载的模块/包名")
            self.msg.config(text="请输入要卸载的模块/包名")
            return None
        self.msg.config(text='卸载中...')
        self.win.update()
        system("CLS")
        print("——" * 10 + "Uninstalling 开始卸载" + "——" * 10 + "\n")
        print("正在卸载", mk)
        system(f"pip uninstall -y {mk}")
        print("\n" + "——" * 10 + "Uninstall-over 卸载结束" + "——" * 10)
        self.msg.config(text='卸载结束')
        return None

    def upgrade(self) -> None:
        mk = self.mk_name.get() + " " + self.mk_version.get()
        if mk == " ":
            print("请输入要升级的模块/包名")
            self.msg.config(text="请输入要升级的模块/包名")
            return None
        self.msg.config(text='升级中...')
        self.win.update()
        system("CLS")
        print("——" * 10 + "开始升级" + "——" * 10 + "\n")
        print("正在升级", mk)
        asyncio.run(PIP.download(mk, "upgrade"))
        print("\n" + "——" * 10 + "升级结束" + "——" * 10)
        self.msg.config(text='升级结束')
        return None

    def show(self) -> None:
        mk = self.mk_name.get()
        if mk == "":
            print("请输入要查看的模块/包名")
            self.msg.config(text="请输入要查看的模块/包名")
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

    def default(self) -> None:
        set_default = PipDefault(self.msg)

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


class PipDefault:

    def __init__(self, msd_obj: tk.Label):
        self.yn = None
        self.msd_obj = msd_obj
        self.win = tk.Tk()
        self.win.geometry("300x200+620+400")
        self.win.title("设置默认PYPI")
        self.win.resizable(False, False)
        self.win.attributes("-topmost", True)
        tk.Label(self.win, text="请选择镜像站设置为默认PYPI").pack()
        tk.Label(self.win, text="默认镜像设置后，\n在命令行窗口运行pip将用您选择的镜像站安装",
                 foreground="blue").pack()
        mirror_station1 = tk.Frame(self.win)
        mirror_station2 = tk.Frame(self.win)
        button_qh = tk.Button(mirror_station1, text="清华镜像站", command=self.def_qh)
        button_qh.pack(side=tk.LEFT)
        button_bw = tk.Button(mirror_station1, text="北外镜像站", command=self.def_bw)
        button_bw.pack(side=tk.LEFT)
        button_db = tk.Button(mirror_station2, text="豆瓣镜像站", command=self.def_db)
        button_db.pack(side=tk.LEFT)
        button_al = tk.Button(mirror_station2, text="阿里镜像站", command=self.def_al)
        button_al.pack(side=tk.LEFT)

        mirror_station1.pack(padx=20)
        mirror_station2.pack(padx=20)
        button_cz = tk.Button(self.win, text="还原为官方PYPI", command=self.def_cz)
        button_cz.pack(side=tk.TOP, ipadx=23)

        self.win.mainloop()

    def default(self, mirror_station_name: str, link: str) -> None:
        yn = mbox.askquestion(title="PIP-GUI", message=f"是否确认将{mirror_station_name}设置为默认")
        if yn == "yes":
            print("开始设置")
            system(f"pip config set global.index-url {link}")
            print("设置完成")
            self.msd_obj.config(text="设置完成")
        else:
            self.msd_obj.config(text="取消设置")
        self.win.destroy()

    def def_qh(self) -> None:
        self.default("清华镜像站", "https://pypi.tuna.tsinghua.edu.cn/simple")

    def def_bw(self) -> None:
        self.default("北外镜像站", "https://pypi.mirrors.ustc.edu.cn/simple")

    def def_db(self) -> None:
        self.default("豆瓣镜像站", "http://pypi.douban.com/simple/")

    def def_al(self) -> None:
        self.default("阿里镜像站", "http://mirrors.aliyun.com/pypi/simple")

    def def_cz(self) -> None:
        self.default("官方PYPI", "https://pypi.org/simple")


PIP = PIP()  # 运行
