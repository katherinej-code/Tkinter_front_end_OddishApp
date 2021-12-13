from tkinter import *
root = Tk()
root.title("Nokia Performance")
root.geometry("583x591+468+158")
root.title("NOKIA _ANSI Performance")
root.configure(borderwidth="1")
root.configure(relief="sunken")
root.configure(background="#dbd8d7")
root.configure(cursor="arrow")
root.configure(highlightbackground="#d9d9d9")
root.configure(highlightcolor="black")


Label1 = Label(root)
_img1 = PhotoImage(file="C:/Users/kathj/Desktop/Flower_proj_front-end/Logo.png")
Label1.configure(image=_img1)
Label1.configure(text='''Label''')
Label1.pack()

Label2 = Label(root)
Label2.configure(text='''Enter the platform :''')
Label2.pack(side=LEFT)

Entry2 = Entry(root)
Entry2.pack(side = RIGHT)

Label3 = Label(root)
Label3.configure(text='''Device  IP Address :''')
Label3.pack()

Entry5 = Entry(root)
Entry5.pack()

Label5 = Label(root)
Label5.configure(text='''Username :''')
Label5.pack()

Label6 = Label(root)
Label6.configure(text='''Label''')
Label6.pack()

Label7 = Label(root)
Label7.configure(text='''Craft IP :''')
Label7.pack()

Label8 = Label(root)
Label8.configure(text='''GICCI IP :''')
Label8.pack()

Label9 = Label(root)
Label9.configure(text='''Password :''')
Label9.pack()

Label10 = Label(root)
Label10.configure(text='''STC File Location''')
Label10.pack()

Label11 = Label(root)
Label11.configure(text='''STC Port :''')
Label1.pack()

Label12 = Label(root)
Label12.configure(text='''STC IP :''')
Label2.pack()


Entry6 = Entry(root)
Entry6.configure(background="white")
Entry6.configure(foreground="#000000")
Entry6.pack()

Entry7 = Entry(root)
Entry7.configure(background="white")
Entry7.pack()

Entry8 = Entry(root)
Entry8.configure(background="white")
Entry8.pack()

Entry9 = Entry(root)
Entry9.configure(background="white")
Entry9.configure(foreground="#000000")
Entry9.pack()

Entry10 = Entry(root)
Entry10.configure(background="white")
Entry10.configure(foreground="#000000")
Entry10.pack()

Entry11 = Entry(root)
Entry11.configure(background="white")
Entry11.configure(foreground="#000000")
Entry11.pack()

Radiobutton1 = Radiobutton(root)
Radiobutton1.configure(justify=LEFT)
Radiobutton1.configure(text='''NRNT-A''')
Radiobutton1.pack()

Radiobutton2 = Radiobutton(root)
Radiobutton2.configure(justify=LEFT)
Radiobutton2.configure(text='''SX-12VP''')
Radiobutton2.pack()

Radiobutton3 = Radiobutton(root)
Radiobutton3.configure(justify=LEFT)
Radiobutton3.configure(text='''DX-48''')
Radiobutton3.pack()

Radiobutton4 = Radiobutton(root)
Radiobutton4.configure(justify=LEFT)
Radiobutton4.configure(text='''SX-16VP''')
Radiobutton4.pack()

Radiobutton5 = Radiobutton(root)
Radiobutton5.configure(justify=LEFT)
Radiobutton5.configure(text='''SX-16F''')
Radiobutton5.pack()

Radiobutton6 = Radiobutton(root)
Radiobutton6.configure(justify=LEFT)
Radiobutton6.configure(text='''FX-8''')
Radiobutton6.pack()

Button1 = Button(root)
Button1.configure(pady="0")
Button1.configure(text='''NEXT''')
Button1.pack()
mainloop()