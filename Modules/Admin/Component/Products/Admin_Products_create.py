from tkinter import *


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

    @staticmethod
    def generate_products_form(obj):
        # create form in form frame
        obj.product_id_label = Label(obj.formframe, text="Product ID:", font=("Arial", 12, "bold"), bg='#ffffff')
        obj.product_id_label.place(x=250, y=290, width=125, height=25)
        obj.product_id_entry = Entry(obj.formframe, font=('Arial', 12))
        obj.product_id_entry.place(x=435, y=285, width=445, height=35)

        obj.product_name_label = Label(text="Product name:", font=("Arial", 12, 'bold'), bg='#ffffff')
        obj.product_name_label.place(x=250, y=340, width=160, height=25)
        obj.product_name_entry = Entry(obj.formframe, font=('Arial', 12))
        obj.product_name_entry.place(x=435, y=335, width=445, height=35)

        obj.description_label = Label(text="Description:", font=("Arial", 12, "bold"), bg='#ffffff')
        obj.description_label.place(x=250, y=390, width=130, height=25)
        obj.description_entry = Entry(obj.formframe, font=('Arial', 12))
        obj.description_entry.place(x=435, y=385, width=445, height=35)

        obj.category_label = Label(text="Category:", font=("Arial", 12, "bold"), bg='#ffffff')
        obj.category_label.place(x=250, y=440, width=105, height=25)
        obj.category_entry = Entry(obj.formframe, font=('Arial', 12))
        obj.category_entry.place(x=435, y=435, width=445, height=35)

        obj.price_label = Label(text="Price:", font=("Arial", 12, "bold"), bg='#ffffff')
        obj.price_label.place(x=250, y=490, width=65, height=25)
        obj.price_entry = Entry(obj.formframe, font=('Arial', 12))
        obj.price_entry.place(x=435, y=485, width=445, height=35)

        obj.stock_label = Label(text="Stock:", font=("Arial", 12, "bold"), bg='#ffffff')
        obj.stock_label.place(x=250, y=540, width=70, height=25)
        obj.stock_entry = Entry(obj.formframe, font=('Arial', 12))
        obj.stock_entry.place(x=435, y=535, width=445, height=35)

    @staticmethod
    def generate_products_button(obj):
        obj.add_button = Button(obj.buttonframe, text="Add item", font=("Arial", 12, "bold"), bg='#ffffff')
        obj.add_button.place(x=330, y=640, width=175, height=40)

        obj.back_button = Button(obj.buttonframe, text="Back", font=("Arial", 12, "bold"), bg='#ffffff')
        obj.back_button.place(x=580, y=640, width=175, height=40)
