from tkinter import *

k=0
def klikker(event):
    global k
    k+=1
    btn.configure(text=k)

def klikkermaha(event):
    global k
    k-=1
    btn.configure(text=k)

def tekst_to_lbl(event):
    t=ent.get()
    lbl.configure(text=t)
    ent.delete(0,END)


aken=Tk()
aken.geometry('700x300')
aken.title('Ruutvõrrandid')


lbl=Label(aken,text='Ruutvõrrandi lahendamine',bg='gold',fg='#AA4A44',font='Arial 20',height=2,width=20)
lbl2=Label(aken,text='x**2+',font='Arial 20',height=2,width=5)
lbl3=Label(aken,text='x+',font='Arial 20',height=2,width=5)
lbl4=Label(aken,text='=0',font='Arial 20',height=2,width=5)
btn=Button(aken,text='Otsustama',font='Arial 24',relief=RAISED)
ent=Entry(aken,fg='blue',bg='Lightblue',width=5,font='Arial 20',justify=CENTER)
ent2=Entry(aken,fg='blue',bg='Lightblue',width=5,font='Arial 20',justify=CENTER)
ent3=Entry(aken,fg='blue',bg='Lightblue',width=5,font='Arial 20',justify=CENTER)

btn.bind('<Button-1>',klikker) 
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


aken.mainloop()
