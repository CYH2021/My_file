import math
import tkinter as tk


def out_fam1():
    a, b, c = int(ent1.get()), int(ent2.get()), int(ent3.get())
    s = 1 / 2 * (a + b + c)
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    text = '三角形面积为: {0:.5}'.format(area)
    # show_lab.config()
    text1.delete(1.0, 'end')
    text1.insert('insert', text)


def out_bind_fam1(event):
    out_fam1()
    return event


def cst():
    # print(ent.get(), end=':')
    # print(type(ent.get()))

    for i in ent.get():
        if i in '.0123456789':
            pass
        else:
            lab.config(text='请输入数字！')
            raise ValueError('请输入数字！')

    in_ = float(ent.get())
    rad = in_ * math.pi / 180
    sin_str = 'sin {0}°= {1:<06.4}\n'.format(in_, math.sin(rad))
    cos_str = 'cos {0}°= {1:<06.4}\n'.format(in_, math.cos(rad))
    tan_str = 'tan {0}°= {1:<06.4}\n'.format(in_, math.tan(rad))

    lab_str = sin_str + cos_str + tan_str
    text2.delete(1.0, 'end')
    text2.insert('insert', lab_str)
    # lab.config(text=lab_str)


def cst_bind(event):
    cst()
    return event


win = tk.Tk()
win.title('三角计算')
win.geometry('500x260')
win.resizable(False, False)

fam1 = tk.Frame(win)
tk.Label(fam1, text='计算三角形面积').pack()
tk.Label(fam1, text='请输入第一个边').pack(anchor=tk.W)
ent1 = tk.Entry(fam1)
ent1.pack(anchor=tk.W, padx=10, fill=tk.X)
tk.Label(fam1, text='请输入第二个边').pack(anchor=tk.W)
ent2 = tk.Entry(fam1)
ent2.pack(anchor=tk.W, padx=10, fill=tk.X)
tk.Label(fam1, text='请输入第三个边').pack(anchor=tk.W)
ent3 = tk.Entry(fam1)
ent3.pack(anchor=tk.W, padx=10, fill=tk.X)
tk.Button(fam1, text='开始计算', command=out_fam1)\
    .pack(pady=10, padx=10, ipadx=50)

fam1.pack(side=tk.LEFT, fill=tk.X, ipadx=40, padx=10)
fam2 = tk.Frame(win)
# show_lab = tk.Label(fam1, text='')
# show_lab.pack(side=tk.TOP)

text1 = tk.Text(fam1, height=1, width=25)
text1.insert('insert', '')
text1.pack()
ent3.bind('<Return>', out_bind_fam1)
fam1.bind('<Return>', out_bind_fam1)

tk.Label(fam2, text='计算三角函数').pack(side=tk.TOP)
tk.Label(fam2, text='请输入度数').pack(side=tk.TOP)
ent = tk.Entry(fam2)
ent.pack(side=tk.TOP)
tk.Button(fam2, text='开始计算', command=cst)\
    .pack(side=tk.TOP, ipadx=50, pady=10)
ent.bind('<Return>', cst_bind)
lab = tk.Label(fam2, text='')
lab.pack(side=tk.TOP)
text2 = tk.Text(fam2, height=5)
text2.insert('insert', '')
text2.pack(side=tk.TOP, fill=tk.Y)
fam2.pack(side=tk.LEFT, fill=tk.X, padx=25)

tk.mainloop()
