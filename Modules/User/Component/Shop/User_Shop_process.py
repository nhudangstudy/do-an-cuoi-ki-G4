from tkinter import * 
from tkinter import ttk
import Api.User_Api as Api
from tkinter import messagebox 
import Service.Widget_service as ws

class User_Shop_process: 
    @staticmethod 
    def generate_shop_table(obj): 
        def clickprodtable(event): 
            #get selected product
            cur = obj.tree.selection()
            cur = obj.tree.item(cur)
            obj.selected_product = cur['values'] 
            obj.product_id.set(cur['values'][0])
            obj.product_name.set(cur['values'][1]) 
            obj.quantity.set(cur['values'][2]) 
            obj.price.set(cur['values'][3]) 

        #create tree view 
        obj.tree = ttk.Treeview(obj.tableframe, columns = ("Product_id", "Product_name", "Quantity", "Price"), height = 20)
        obj.tree.heading("#0") 
        obj.tree.heading("#1", text = "Product_id") 
        obj.tree.heading("#2", text = "Product_name") 
        obj.tree.heading("#3", text = "Quantity") 
        obj.tree.heading("#4", text = "Price") 
        obj.tree.column("#0", width = 0) 
        obj.tree.column("#1", width = 240, stretch=NO) 
        obj.tree.column("#2", width = 240, stretch=NO) 
        obj.tree.column("#3", width = 240, stretch=NO) 
        obj.tree.column("#4", width = 240, stretch=NO)
        obj.tree.bind("<<TreeviewSelect>>", clickprodtable)
        obj.tree.grid(row = 1, column = 0, columnspan = 7, sticky = (N, S, W, E)) 
        #create scrollbar 
        obj.scrollbar = Scrollbar(obj.tableframe, orient = VERTICAL, command = obj.tree.yview) 
        obj.scrollbar.grid(row = 1, column = 7, sticky = (N, S, W, E)) 
        obj.tree.configure(yscrollcommand = obj.scrollbar.set) 
            

        #get product id

    @staticmethod 
    def generate_shop_form(obj): 
        #create form in form frame 
        obj.product_id = StringVar() 
        obj.product_name = StringVar() 
        obj.quantity = StringVar() 
        obj.price = StringVar() 
        obj.total = StringVar() 

        obj.product_id_label = Label(obj.formframe, text = "Product_id:", font = ("Arial", 12, "bold"), bg = "#ffffff") 
        obj.product_id_label.place(x = 10, y = 10, width = 150, height = 30)
        obj.product_id_entry = Entry(obj.formframe, textvariable = obj.product_id, font = ("Arial", 12), state=DISABLED, width= 20)
        obj.product_id_entry.place(x = 160, y = 10, width = 300, height = 30) 

        obj.product_name_label = Label(obj.formframe, text = "Product_name:", font = ("Arial", 12, "bold"), bg = "#ffffff") 
        obj.product_name_label.place(x = 10, y = 50, width = 150, height = 30)
        list = Api.User_Api.get_product_name()     
        obj.product_name_entry = ws.AutofillEntry()
        obj.product_name_entry = Entry(obj.formframe, textvariable = obj.product_name, font = ("Arial", 12), state=DISABLED, width=150)
        obj.product_name_entry.place(x = 160, y = 50, width = 300, height = 30)

        obj.quantity_label = Label(obj.formframe, text = "Quantity:", font = ("Arial", 12, "bold"), bg = "#ffffff")
        obj.quantity_label.place(x = 10, y = 90, width = 150, height = 30)
        obj.quantity_entry = Entry(obj.formframe, textvariable = obj.quantity, font = ("Arial", 12),  state=DISABLED,  width=150)
        obj.quantity_entry.place(x = 160, y = 90, width = 300, height = 30) 
       
        obj.price_label = Label(obj.formframe, text = "Price:", font = ("Arial", 12, "bold"), bg = "#ffffff")
        obj.price_label.place(x = 10, y = 130, width = 150, height = 30)
        obj.price_entry = Entry(obj.formframe, textvariable = obj.price, font = ("Arial", 12),  state=DISABLED,  width=150)
        obj.price_entry.place(x = 160, y = 130, width = 300, height = 30)
        
    @staticmethod 
    def generate_shop_buttons(obj): 
        #process button 
        obj.process_button = Button(obj.buttonframe, text = "Process", font = ("Arial", 12, "bold"), bg = "#ffffff") 
        obj.process_button.place(x = 10, y = 10, width = 100, height = 120)
        
        obj.search_label = Label(obj.buttonframe, text = "Search:", font = ("Arial", 12, "bold"), bg = "#ffffff") 
        obj.search_label.place(x = 120, y = 10, width = 100, height = 30)

        obj.quantity_label = Label(obj.buttonframe, text = "Quantity:", font = ("Arial", 12, "bold"), bg = "#ffffff") 
        obj.quantity_label.place(x = 120, y = 50, width = 100, height = 30)

        #create search entry 
        obj.search_entry = Entry(obj.buttonframe, font = ("Arial", 12), width=20) 
        obj.search_entry.place(x = 240, y = 10, width = 200, height = 30) 
        #create quantity entry 
        obj.quantity_entry = Entry(obj.buttonframe, font = ("Arial", 12), width=20) 
        obj.quantity_entry.place(x = 240, y = 50, width = 200, height = 30) 

        #create add to cart button 
        obj.add_button = Button(obj.buttonframe, text = "Add to cart", font = ("Arial", 12, "bold"), bg = "#ffffff", command = lambda: User_Shop_process.add_to_cart(obj))
        obj.add_button.place(x = 130, y = 100, width = 160, height = 30) 

        #create remove from cart button 
        obj.remove_button = Button(obj.buttonframe, text = "Remove", font = ("Arial", 12, "bold"), bg = "#ffffff") 
        obj.remove_button.place(x = 300, y = 100, width = 160, height = 30) 

        #create total amount label 
        obj.total_label = Label(obj.buttonframe, text = "Total:", font = ("Arial", 20, "bold"), bg = "#ffffff") 
        obj.total_label.place(x = 10, y = 150, width = 100, height = 30)

        #create total amount entry 
        obj.total_entry = Entry(obj.buttonframe, textvariable = obj.total, font = ("Arial", 20), state=DISABLED, width=20)
        obj.total_entry.place(x = 120, y = 150, width = 200, height = 30)

    @staticmethod 
    def add_to_cart(obj): 
        #add to cart 

        obj.quantity.set(obj.quantity_entry.get())
        obj.price.set(obj.price_entry.get())
        api = Api.User_Api()
        check = api.add_item_to_cart(obj.search_entry.get(), obj.quantity.get())
        if check == -1: 
            messagebox.showinfo("Error", "Product not found") 
        elif check == -2: 
            messagebox.showinfo("Error", "Quantity not available") 
        elif check == -3: 
            messagebox.showinfo("Error", "Error quantity") 
        elif check == -4: 

            for item in obj.tree.get_children():
                obj.tree.delete(item)
            #update treeview data 
            data = api.total_cart 
            for item in data: 
                obj.tree.insert("", END, values = (item["Product_id"], item["Product_name"], item["Quantity"], item["Price"]))
                User_Shop_process.get_total_ammount(obj)
            obj.price.set(api.temp)
            messagebox.showinfo("Success", "Item upadated")
        else: 
            #add check to treeview  
            obj.tree.insert("", "end", values = (check['Product_id'], check['Product_name'], check['Quantity'], check['Price']))
            obj.product_id.set(check["Product_id"]) 
            obj.product_name.set(check["Product_name"]) 
            obj.quantity.set(check["Quantity"]) 
            obj.price.set(check["Price"])
            messagebox.showinfo("Success", "Product added to cart") 
            User_Shop_process.get_total_ammount(obj)
        
    @staticmethod 
    def remove_from_cart(obj): 
        #remove from cart 
        api = Api.User_Api() 
        #get choosen data of obj.tree 
        data = obj.tree.item(obj.tree.selection())['values'] 
        #remove from cart 
        api.remove_item_from_cart(data[0]) 

    @staticmethod 
    def get_total_ammount(obj):
        #get total amount 
        api = Api.User_Api() 
        data = api.total_cart 
        total = 0 
        for item in data: 
            total += int(item['Price'])
        obj.total.set(total)
        