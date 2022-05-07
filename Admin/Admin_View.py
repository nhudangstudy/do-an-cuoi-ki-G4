from tkinter import *


class Admin_View:

    def __init__(self):
        self.window = Tk()
        self.window.geometry("1080x720")
        self.window.configure(bg="#ffffff")
        self.window.title('Admin')

        self.canvas = Canvas(self.window, bg="#ffffff", height=720, width=1080,
                             bd=0, highlightthickness=0, relief="ridge")

        self.canvas.place(x=0, y=0)

        # -----background-----
        self.background_img = PhotoImage(file=f"background.png")
        self.background = self.canvas.create_image(708.0, 515.5, image=self.background_img)

        # -----text-----
        self.canvas.create_text(200, 425.5,
                                text="A Sales Management System\nby Group 4 - K21416C",
                                fill="#000000",
                                font=("MontserratRoman-Regular", int(15.0)))

        self.canvas.create_text(420, 297.0,
                                text="ALWAYS THERE \nFOR YOUR BUSINESS",
                                fill="#000000",
                                font=("MontserratRoman-Black", int(50.0), "bold"))

        # -----button-log-out-----
        self.img_log_out = PhotoImage(file=f"./Images/Admin/img_log_out.png")
        self.button_log_out = Button(image=self.img_log_out, borderwidth=0,
                                     highlightthickness=0, relief="flat", bg="#ffffff")

        self.button_log_out.place(x=800, y=60, width=210, height=60)

        # -----button-products-----
        self.img_products = PhotoImage(file=f"./Images/Admin/img_products.png")
        self.button_products = Button(image=self.img_products, borderwidth=0,
                                      highlightthickness=0, relief="flat", bg="#ffffff")

        self.button_products.place(x=49, y=582, width=170, height=55)

        # -----button-inventory-----
        self.img_inventory = PhotoImage(file=f"./Images/Admin/img_inventory.png")
        self.button_inventory = Button(image=self.img_inventory, borderwidth=0,
                                       highlightthickness=0, relief="flat", bg="#ffffff")

        self.button_inventory.place(x=219, y=582, width=170, height=55)

        # -----button-sales-----
        self.img_sales = PhotoImage(file=f"./Images/Admin/img_sales.png")
        self.button_sales = Button(image=self.img_sales, borderwidth=0, highlightthickness=0,
                                   relief="flat", bg="#ffffff")

        self.button_sales.place(x=389, y=582, width=170, height=55)

        # -----button-users-----
        self.img_users = PhotoImage(file=f"./Images/Admin/img_users.png")
        self.button_users = Button(image=self.img_users, borderwidth=0, highlightthickness=0,
                                   relief="flat", bg="#ffffff")

        self.button_users.place(x=559, y=582, width=170, height=55)
