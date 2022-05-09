from tkinter import * 
import Modules.User.Component.Shop.User_Shop_process as usp

class User_Shop_create:
    @staticmethod 
    def generate_shop(obj):
        #clear all frames 
        for frame in obj.allframes:
            frame.place_forget()
        obj.allframes = [] 
        #create new frames 
        obj.tableframe = Frame(obj.window, bg = "pink") 
        obj.tableframe.place(x = 50, y = 250, width = 980, height = 200)

        obj.formframe = Frame(obj.window, bg = "pink")
        obj.formframe.place(x = 50, y = 480, width = 480, height = 200) 

        obj.buttonframe = Frame(obj.window, bg = "pink") 
        obj.buttonframe.place(x = 550, y = 480, width = 480, height = 200) 

        obj.allframes.append(obj.tableframe)    
        obj.allframes.append(obj.formframe)
        obj.allframes.append(obj.buttonframe) 

        #create table 
        usp.User_Shop_process.generate_shop_table(obj) 
        #create form 
        usp.User_Shop_process.generate_shop_form(obj) 
        #create buttons 
        usp.User_Shop_process.generate_shop_buttons(obj) 

