'''
1.导入tkinter组建
2.实例化Tk()类对象root
3.在root中 实例化LabelFrame类对象group
4.显示group  padx=10 pad=10
5.创建LANGS列表
6.实例化IntVar类对象v
7.v.set()方法设置v=1
8.在group中 实例化Radiobutton类对象b
9.b.pack   anchor=W   靠西，即使靠左
10.mainloop()
'''

from tkinter import *

root = Tk()

group = LabelFrame(root,text="最好的脚本语言是？",padx=5,pady=5)
group.pack(padx=10,pady=10)

LANGS = [("pthon",1),("perl",2),("ruby",3),("lua",4)]

v=IntVar()
v.set(1)

for langs,num in LANGS:
    b = Radiobutton(group,text=langs,variable=v,value=num)
    b.pack(anchor = E)

mainloop()
