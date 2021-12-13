from tkinter import *

root = Tk()
root.title("Login UI using Pack")
root.geometry("400x320")  # set starting size of window
root.maxsize(400, 320)  # width x height
root.config(bg="#6FAFE7")  # set background color of root window

login = Label(root, text="Login", bg="#2176C1", fg='white', relief=RAISED)
login.pack(ipady=5, fill='x')
login.config(font=("Font", 30))  # change font and size of label

# login image
image = PhotoImage(file="nLogo.png")
img_resize = image.subsample(2, 2)
Label(root, image=img_resize, bg="#6FAFE7").pack(pady=5)

root.mainloop()