from tkinter import *
def Mysel():
    dic={0:'甲',1:'乙',2:'丙'}
    s="您选了"+dic.get(var.get())+"项"
    lb.config(text=s)

root=Tk()
root.geometry('320x240')
lb=Label(root)
lb.pack()

var=IntVar() #声明的变量，在调用的函数中方可用var.get()方法取得被选中实例的value值
rd1=Radiobutton(root,text="甲-llllll",variable=var,value=0,command=Mysel)
rd1.pack()
rd2=Radiobutton(root,text="乙-llllll",variable=var,value=1,command=Mysel)
rd2.pack()
rd3=Radiobutton(root,text="丙-llllll",variable=var,value=2,command=Mysel)
rd3.pack()

root.mainloop()