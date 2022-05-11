from cgitb import reset
from tkinter import * 
import Api.Admin_Api as AdminApi
import Modules.Admin.Component.Inventory.Admin_Inventory_create as aic
import Api.Main_Api as MainApi 
import tkinter.messagebox as mbox

class Admin_Inventory_Process:
    @staticmethod
    def get_json_data(obj):
        product_name = obj.product_name_entry.get()
        description = obj.description_entry.get()
        category = obj.category_entry.get()
        price = obj.price_entry.get()
        current_stock = obj.current_stock_entry.get()
        add_stock = obj.add_stock_entry.get()
        if product_name == '' or description == '' or category == '' or price == '' or current_stock == '' or add_stock == '':
            mbox.showerror('Error','Invalid User Input')
        else:
            obj.json_data = {
                'Product_name': f'{product_name}',
                'Description' : f'{description}',
                'Category': f'{category}',
                'Price': f'{price}',
                'Stock': f'{current_stock}',
            }

    @staticmethod
    def update_button_handle(obj):
        data = Admin_Inventory_Process.get_json_data(obj)
        api = AdminApi.Admin_Api()
        check = api.Admin_Api.update_items(data)
        if check == -2:
            mbox.showerror('Error','product id is not in collection but all informations are in collection')
        else:
            for item in obj.tree.get_children():
                obj.tree.delete(item)
            for i in range(len(data)):
                obj.tree.insert()
            
            mbox.showinfo('Success','Update successful')
        reset(obj)

    @staticmethod
    def remove_button_handle(obj):
        api = AdminApi.Admin_Api()
        data = obj.json_data
        remove = api.remove_items(data)
        mbox.showinfo('Success','Remove successful')
        reset(obj)

    @staticmethod
    def reset(obj):
        obj.product_name_entry.delete(0,END)
        obj.description_entry.delete(0,END)
        obj.category_entry.delete(0,END)
        obj.price_entry.delete(0,END)
        obj.current_stock_entry.delete(0,END)
        obj.add_stock_entry.delete(0,END)