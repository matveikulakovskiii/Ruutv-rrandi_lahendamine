from tkinter import *
from math import *
import numpy as np
import matplotlib.pyplot as plt 

k=0
def grafik():
    ent_=float(ent.get())
    ent2_=float(ent2.get())
    ent3_=float(ent3.get())
    x0=(-ent2_)/2*ent_ 
    y0=ent_*x0*x0+ent2_*x0+ent3_
    x=np.arange(x0-15,x0+15,1)#min,max,step
    y=ent_*x*x+ent2_*x+ent3_
    fig=plt.figure()
    plt.plot(x,y,'r-d')
    plt.title('Ruutvõrrand')
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.grid(True)
    plt.show()


def klikkermaha(event):
    global k
    k-=1
    btn.configure(text=k)

def tekst_to_lbl(event):
    t=ent.get()
    lbl.configure(text=t)
    ent.delete(0,END)

def lahenda():
    if ent.get()=='': ent.configure(bg='red')
    else:
        ent.configure(bg='Lightblue')
    if ent2.get()=='': ent2.configure(bg='red')
    else:
        ent2.configure(bg='Lightblue')
    if ent3.get()=='': ent3.configure(bg='red')
    else:
        ent3.configure(bg='Lightblue')
    if ent.get()!='' and ent2.get()!='' and ent3.get()!='':
        ent_=float(ent.get())
        ent2_=float(ent2.get())
        ent3_=float(ent3.get())
        D=ent2_*ent2_-4*ent_*ent3_
        if D>0:
            x1=round((-1*ent2-sqrt(D))/(2*ent),2)
            x2=round((-1*ent2-sqrt(D))/(2*ent),2)
            vas=f'X1={x1} \nx2={x2}'
        elif D==0:
            x1=round(-1*ent2/(2*ent),2)
            vas=f'X1={x1}'
        else:
            vastus='Lahendust pole'
        vastus.configure(text=vas)








aken=Tk()
aken.geometry('700x300')
aken.title('Ruutvõrrandid')


lbl=Label(aken,text='Ruutvõrrandi lahendamine',bg='gold',fg='#AA4A44',font='Arial 20',height=2,width=20)
lbl2=Label(aken,text='x**2+',font='Arial 20',height=2,width=5)
lbl3=Label(aken,text='x+',font='Arial 20',height=2,width=5)
lbl4=Label(aken,text='=0',font='Arial 20',height=2,width=5)
btn=Button(aken,text='Lahenda',font='Arial 24',relief=RAISED,command=lahenda)
btn2=Button(aken,text='Graafika',font='Arial 24',relief=RAISED,command=lahenda)
ent=Entry(aken,fg='blue',bg='Lightblue',width=5,font='Arial 20',justify=CENTER)
ent2=Entry(aken,fg='blue',bg='Lightblue',width=5,font='Arial 20',justify=CENTER)
ent3=Entry(aken,fg='blue',bg='Lightblue',width=5,font='Arial 20',justify=CENTER)

btn.bind('<Button-1>') 
btn.bind('<Button-3>',klikkermaha) 
ent.bind('<Return>',tekst_to_lbl)
ent2.bind('<Return>',tekst_to_lbl) 
ent3.bind('<Return>',tekst_to_lbl) 
lbl.pack(side=TOP) 
btn.pack(side=RIGHT)
ent.pack(side=LEFT)
lbl2.pack(side=LEFT) 
ent2.pack(side=LEFT)
lbl3.pack(side=LEFT) 
ent3.pack(side=LEFT)
lbl4.pack(side=LEFT) 
grafik


aken.mainloop()
