from tkinter import *
import Modules.Admin.Component.Products.Admin_Products_process as admin_pp


class Admin_Products_create:

    @staticmethod
    def generate_products(obj):
        # clear all frames
        for frame in obj.allframes:
            frame.place_forget()
        obj.allframes = []

        # create new frames
        obj.formframe = Frame(obj.window, bg='#fccde0')
        obj.formframe.place(x=205, y=255, width=730, height=350)

        obj.buttonframe = Frame(obj.window, bg="#ffffff")
        obj.buttonframe.place(x=315, y=630, width=450, height=65)
        obj.allframes.append(obj.formframe)
        obj.allframes.append(obj.buttonframe)

        # Generate product button and product form
        Admin_Products_create.generate_products_button(obj)
        Admin_Products_create.generate_products_form(obj)

    @staticmethod
    def generate_products_form(obj):
        # create form in form frame
        obj.product_id_label = Label(obj.formframe, text="Product ID:", font=("Arial", 12, "bold"), bg='#ffffff')
        obj.product_id_label.place(x=45, y=35, width=125, height=25)
        obj.product_id_entry = Entry(obj.formframe, font=('Arial', 12))
        obj.product_id_entry.place(x=230, y=30, width=445, height=35)

        obj.product_name_label = Label(obj.formframe, text="Product name:", font=("Arial", 12, 'bold'), bg='#ffffff')
        obj.product_name_label.place(x=45, y=85, width=160, height=25)
        obj.product_name_entry = Entry(obj.formframe, font=('Arial', 12))
        obj.product_name_entry.place(x=230, y=80, width=445, height=35)

        obj.description_label = Label(obj.formframe, text="Description:", font=("Arial", 12, "bold"), bg='#ffffff')
        obj.description_label.place(x=45, y=135, width=130, height=25)
        obj.description_entry = Entry(obj.formframe, font=('Arial', 12))
        obj.description_entry.place(x=230, y=130, width=445, height=35)

        obj.category_label = Label(obj.formframe, text="Category:", font=("Arial", 12, "bold"), bg='#ffffff')
        obj.category_label.place(x=45, y=185, width=105, height=25)
        obj.category_entry = Entry(obj.formframe, font=('Arial', 12))
        obj.category_entry.place(x=230, y=180, width=445, height=35)

        obj.price_label = Label(obj.formframe, text="Price:", font=("Arial", 12, "bold"), bg='#ffffff')
        obj.price_label.place(x=45, y=235, width=65, height=25)
        obj.price_entry = Entry(obj.formframe, font=('Arial', 12))
        obj.price_entry.place(x=230, y=230, width=445, height=35)

        obj.stock_label = Label(obj.formframe, text="Stock:", font=("Arial", 12, "bold"), bg='#ffffff')
        obj.stock_label.place(x=45, y=285, width=70, height=25)
        obj.stock_entry = Entry(obj.formframe, font=('Arial', 12))
        obj.stock_entry.place(x=230, y=280, width=445, height=35)

    @staticmethod
    def generate_products_button(obj):
        obj.add_button = Button(obj.buttonframe, text="Add item", font=("Arial", 12, "bold"), bg='#ffffff', command=lambda: admin_pp.Admin_Products_Process.add_item_button_handle(obj))
        obj.add_button.place(x=15, y=10, width=175, height=40)

        obj.back_button = Button(obj.buttonframe, text="Reset", font=("Arial", 12, "bold"), bg='#ffffff', command=lambda: admin_pp.Admin_Products_Process.back_button_handle(obj))
        obj.back_button.place(x=265, y=10, width=175, height=40)
