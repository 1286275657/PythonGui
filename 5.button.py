'''
1.导入tkinter
2.创建callback()函数
3.实例化Tk()类对象root
4.窗体中创建框架部件对象frame1和frame2，类Frame
5.1.创建StringVar()类对象var，StringVar()类有set()方法
5.2.frame1中创建Label()类文字对象，文字换行左对齐，文字整体居左
6.1.创建PhotoImage()类对象photo
6.2.frame中创建Label()类图片对象
7.frame2添加按钮Button()类对象
8.显示frame1和frame2，padx=10,pady=10
9.mainloop()

其作用是创建个文本图片frame1,和按钮frame2
点击按钮frame2,frame1中的文字变成callback()中指定的文字
'''
from tkinter import *

def callback():
    var.set("我才不信呢！")

root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set("未满18岁禁止观看，\n请18岁后再观看！")

textlabel=Label(frame1,textvariable=var,justify=LEFT)
textlabel.pack(side=LEFT)

photo = PhotoImage(file = "18.PNG")
imglabel = Label(frame1,image=photo)
imglabel.pack(side=RIGHT)

thebutton = Button(frame2,text="已满18岁",command=callback)
thebutton.pack()

frame1.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)

mainloop()