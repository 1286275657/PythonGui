#导入模块
from tkinter import *

#实例化窗口主体Tk()类为对象root
root=Tk()

#创建Label类的名称为textlabel的对象，并将其指定到窗体root对象中。
textlabel = Label(root,text="您下载的影片包含未成年人限制内容！")
#利用pack方法使得textlabel的位置左对齐于窗体
textlabel.pack(side=LEFT)

#用PhotoImage类实例化一个图片对象
photo = PhotoImage(file="18.PNG")
#用Label类实例化名为imglabel的图片对象，并将其显示在root窗体中
imglabel=Label(root,image=photo)
imglabel.pack(side=RIGHT)

mainloop()


'''
1.导入tkinter
2.实例化窗体类 Tk()
3.创建文字Label(),并加载到Tk()对象中，使文字左对齐
4.创建图片Label(),并加载到Tk()对象中，使图片右对齐

mainloop()循环
'''