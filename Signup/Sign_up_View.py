from tkinter import *
import tkinter as tk

class Sign_up_View:

    def __init__(self):
        self.window = Tk() 
        self.window.geometry("1080x720+80+20")
        self.window.title("Signup Page")
        self.window.configure(bg = "#f6efff")
        self.window.iconphoto(False, PhotoImage(file = f"./Images/SignUp/AppIcon.png"))

        self.canvas = Canvas(self, bg = "#f6efff", height = 768, width = 1366, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"./Images/SignUp/background.png")
        self.background = self.canvas.create_image(672.0, 364.0, image=self.background_img)

        self.signup_image = PhotoImage(file = f"./Images/SignUp/Button_SignUp.png")
        self.signup_button = Button(image = self.signup_image, borderwidth = 0, highlightthickness = 0, relief = "flat", bg = "#E3CEFF")
        self.signup_button.place(x=938.75, y=616.54, width=169.66, height=44.42)

        self.signin_image = PhotoImage(file = f"./Images/SignIn/Button_SignIn.png")
        self.signin_button = Button(image = self.signin_image, borderwidth = 0, highlightthickness = 0, relief = "flat", bg = "#E3CEFF")
        self.signin_button.place(x=938.75, y=678.9, width=169.66, height=44.42)

        self.entry_image = PhotoImage(file = f"./Images/SignUp/Textbox.png")
        self.entry_bg1 = self.canvas.create_image(788.0, 523.0, image=self.entry_image)
        self.entry_bg2 = self.canvas.create_image(788.0, 379.0, image=self.entry_image)
        self.entry_bg3 = self.canvas.create_image(788.0, 235.0, image=self.entry_image)

        self.username_entry = Entry(self.window, bd = 0, bg = "#E9D9FF", highlightthickness = 0)
        self.username_entry.place(x = 663.0, y = 398.0, height = 42.0, width = 382.0)

        self.password_entry = Entry(self.window, bd = 0, bg = "#E9D9FF", highlightthickness = 0)
        self.password_entry.place(x = 663.0, y = 254.0, height = 42.0, width = 382.0)

        self.reenterpass_entry = Entry(self.window, bd = 0, bg = "#E9D9FF", highlightthickness = 0)
        self.reenterpass_entry.place(x = 663.0, y = 110.0, height = 42.0, width = 382.0)



app = Sign_up_View()
app.window.mainloop()