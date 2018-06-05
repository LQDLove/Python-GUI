from tkinter import *
def ini():
    Lstbox1.delete(0,END)
    list_items=["数学","物理","化学","语文","外语"]
    for item in list_items:
        Lstbox1.insert(END,item)
    list_credits=[2.0,2.5,1.0,1.5,2.0]
    for item in list_credits:
        Lstbox2.insert(END,item)

def slecurse1(event):
    s='已选'+Lstbox1.get(Lstbox1.curselection())+\
        str(Lstbox2.get(Lstbox1.curselection()))+'学分\n'
    txt.insert(END,s)

def slecurse2(event):
    s = '已选' + Lstbox1.get(Lstbox2.curselection()) + \
        str(Lstbox2.get(Lstbox2.curselection())) + '学分\n'
    txt.insert(END, s)





root=Tk()
root.title('单击课程或学分均可选课')
root.geometry('320x240')
frame1=Frame(root,relief=RAISED)
frame1.place(relx=0.0)
frame2=Frame(root,relief=GROOVE)
frame2.place(relx=0.3)
frame3=Frame(root,relief=RAISED)
frame3.place(relx=0.6)

Lstbox1=Listbox(frame1)
Lstbox1.bind('<ButtonRelease-1>',slecurse1)
Lstbox1.pack()
Lstbox2=Listbox(frame2)
Lstbox2.bind('<ButtonRelease-1>',slecurse2)
Lstbox2.pack()

txt=Text(frame3,height=14,width=18)
txt.pack()
ini()
root.mainloop()
