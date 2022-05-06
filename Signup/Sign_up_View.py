from tkinter import *

class Sign_up_View:

    def __init__(self):
        self.window = Tk() 
        self.window.geometry("1080x720+210+50")
        self.window.title("Signup Page")
        self.window.configure(bg = "#f6efff")
        self.window.iconphoto(False, PhotoImage(file = f"./Images/SignUp/AppIcon.png"))

        self.canvas = Canvas(self.window, bg = "#f6efff", height = 768, width = 1366, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"./Images/SignUp/Background.png")
        self.background = self.canvas.create_image(540, 360, image=self.background_img)

        self.signup_image = PhotoImage(file = f"./Images/SignUp/Button_Signup.png")
        self.signup_button = Button(self.window, image = self.signup_image, borderwidth = 0, highlightthickness = 0, relief = "flat", bg = "#E3CEFF")
        self.signup_button.place(x=723, y=553, width=149, height=40)

        self.signin_image = PhotoImage(file = f"./Images/SignUp/Button_Signin.png")
        self.signin_button = Button(self.window, image = self.signin_image, borderwidth = 0, highlightthickness = 0, relief = "flat", bg = "#E3CEFF")
        self.signin_button.place(x=723, y=615, width=149, height=40)

        self.entry_image = PhotoImage(file = f"./Images/SignUp/Textbox.png")
        self.entry_bg1 = self.canvas.create_image(797, 490, image=self.entry_image)
        self.entry_bg2 = self.canvas.create_image(797, 363, image=self.entry_image)
        self.entry_bg3 = self.canvas.create_image(797, 236, image=self.entry_image)

        self.username_entry = Entry(self.window, bd = 0, bg = "#E3CEFF", highlightthickness = 0)
        self.username_entry.place(x = 605, y = 214, height = 38, width = 382)

        self.password_entry = Entry(self.window,show="*", bd = 0, bg = "#E3CEFF", highlightthickness = 0)
        self.password_entry.place(x = 605, y = 341, height = 38, width = 382)

        self.reenterpass_entry = Entry(self.window,show="*", bd = 0, bg = "#E3CEFF", highlightthickness = 0)
        self.reenterpass_entry.place(x = 605, y = 468, height = 38, width = 382)