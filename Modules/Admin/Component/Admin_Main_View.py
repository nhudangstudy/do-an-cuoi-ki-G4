from re import A
from tkinter import *
import Modules.Admin.Admin_Landing_Process as alp
import Modules.Admin.Component.Inventory.Admin_Inventory_create as aic 
import Modules.Admin.Component.Products.Admin_Products_create as apc
class Admin_Main_View:
    def __init__(self):

        self.window = Tk()

        # get screen width and height
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        # set window width and height
        self.window_width = 1080
        self.window_height = 720
        # set window position
        self.window.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height,
                                              (self.screen_width - self.window_width) / 2,
                                              (self.screen_height - self.window_height) / 2))


        self.window.configure(bg = "#ffffff")
        self.window.title('Admin Main Page')

        self.allframes = []

        self.canvas = Canvas(self.window,bg = "#ffffff",height = 720,width = 1080,
                             bd = 0,highlightthickness = 0,relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        # -----background-----
        self.img_background = PhotoImage(file = f"./Images/Admin/MainPage/background.png")
        self.background = self.canvas.create_image(540,65,image = self.img_background)
        

        #-----button-products-----
        self.img_products = PhotoImage(file = f"./Images/Admin/MainPage/img_products.png")
        self.button_products = Button(image = self.img_products,borderwidth = 0,
                                      highlightthickness = 0,relief = "flat", bg="#ffffff", command = lambda: self.click_button("products"))

        self.button_products.place(x = 30, y = 160,width = 150,height = 50)

        #-----button-inventory-----
        self.img_inventory = PhotoImage(file = f"./Images/Admin/MainPage/img_inventory.png")
        self.button_inventory = Button(image = self.img_inventory,borderwidth = 0,
                                       highlightthickness = 0,relief = "flat", bg="#ffffff", command = lambda: self.click_button("inventory"))

        self.button_inventory.place(x = 200, y = 160,width = 150,height = 50)

        #-----button-sales-----
        self.img_sales = PhotoImage(file = f"./Images/Admin/MainPage/img_sales.png")
        self.button_sales = Button(image = self.img_sales,borderwidth = 0,
                                   highlightthickness = 0,relief = "flat", bg="#ffffff")

        self.button_sales.place(x = 380, y = 160,width = 150,height = 50)

        #-----button-users-----
        self.img_users = PhotoImage(file = f"./Images/Admin/MainPage/img_users.png")
        self.button_users = Button(image = self.img_users,borderwidth = 0,
                                   highlightthickness = 0,relief = "flat", bg="#ffffff")

        self.button_users.place(x = 550, y = 160,width = 150,height = 50)

        #-----button-switch-account-----
        self.img_switch = PhotoImage(file = f"./Images/Admin/MainPage/img_switch.png")
        self.button_switch = Button(image = self.img_switch,borderwidth = 0,
                                    highlightthickness = 0,relief = "flat", bg="#ffffff")

        self.button_switch.place(x = 730, y = 160,width = 150,height = 50)

        #-----button-exit-----
        self.img_exit = PhotoImage(file = f"./Images/Admin/MainPage/img_exit.png")
        self.button_exit = Button(image = self.img_exit,borderwidth = 0,
                                  highlightthickness = 0,relief = "flat", bg="#ffffff")

        self.button_exit.place(x = 900, y = 160,width = 150,height = 50)

    def click_button(self,button):
        if button == "products": 
            apc.Admin_Products_create.generate_products(self)
        elif button == "inventory": 
            aic.Admin_Inventory_create.generate_inventory(self)
        elif button == "sales": 
            pass 
        elif button == "users": 
            pass

