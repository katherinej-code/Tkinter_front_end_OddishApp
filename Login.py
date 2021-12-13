from tkinter import messagebox
from tkinter import *
from PIL import ImageTk, Image
import pymysql


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("Login and Registration System for Oddish")
        self.root.geometry("1199x700+100+50")
        self.root.resizable(False, False)

        # Background Image
        self.bg = ImageTk.PhotoImage(file="bg1.jpg")
        self.bg_image=Label(self.root, image=self.bg).place(x=0,y=0, relwidth=1, relheight=1)

        # Login Frame
        Frame_login=Frame(self.root, bg="pale green", highlightbackground="SeaGreen3", highlightthickness=2)
        Frame_login.place(x=400, y=50, height=550, width=400)

        title = Label(Frame_login, text="Welcome to", font=("Century Gothic", 12), fg = "#434343", bg= "pale green").place(x= 160, y=25)

        image = Image.open("nLogo.png")
        resize_image = image.resize((250, 140))
        img = ImageTk.PhotoImage(resize_image)

        # Photo = ImageTk.PhotoImage(image)
        label1 = Label(Frame_login, image=img, bg="pale green")
        label1.image = img
        label1.pack(pady=60)

        # LOGIN label
        desc = Label(Frame_login, text="LOGIN", font=("Century Gothic", 20), fg="#434343", bg="pale green").place(x=168, y=240)

        # Username box
        label2 = Label(Frame_login, text="Username", font=("Century Gothic", 15, "bold"), fg="#434343", bg="pale green").place(x=50, y=300)
        self.txt_user = Entry(Frame_login, font=("Century Gothic", 15, "bold"), bg='lightgray')
        self.txt_user.place(x=50, y=330, width=300, height=35)

        # Password box
        label3 = Label(Frame_login, text="Password", font=("Century Gothic", 15, "bold"), fg="#434343", bg="pale green").place(x=50, y=370)
        self.txt_pass = Entry(Frame_login, font=("Century Gothic", 15, "bold"), bg='lightgray')
        self.txt_pass.place(x=50, y=400, width=300, height=35)

        # Forgot button
        forgot_button = Button(Frame_login, text="Forgot password?", font=('times new roman', 10, "bold"), bg='white', fg='black', bd=0)
        forgot_button.place(x=150, y=450)

        # Login button
        login_button = Button(self.root, text="Login", font=("Century Gothic", 15), fg="white", bg="forest green", width=15, height=1)
        login_button.place(x=250, y=560)



root = Tk()
obj = Login(root)
root.mainloop()
