from tkinter import messagebox
import Api.Main_Api as main_api 
import json
import datetime 

class User_Api(main_api.Api): 
    total_cart = []
    temp = 0
    def __init__(self): 
        super().__init__() 
        self.connector() 
       
    # get last Invoice_Id from invoice collection 
    def get_last_invoice_id(self): 
        self.cursor = self.invoices_collection.find().sort([('Invoice_Id', -1)]) 
        self.last_invoice_id = self.cursor[0]['Invoice_Id']
        return self.last_invoice_id

    def create_new_invoice_id(self): 
        self.last_invoice_id = self.get_last_invoice_id() 
        id = self.last_invoice_id.split('-')[-1]
        new_id = int(id) + 1
        self.new_invoice_id = 'INV-' + str(100+new_id).replace("1","0",1)
        return self.new_invoice_id

    def create_new_invoice(self, invoice_data): 
        self.invoices_collection.insert_one(invoice_data)
        return 0 #success
    
    def add_item_to_cart(self, product_name, quantity):
        data = self.warehouse_collection.find_one({'Product_name': product_name})
        if data == None: 
            return -1 #error 1: product is not exist 
        else: 
            product_id =data['Product_id'] 
            product_name =data['Product_name']
            product_price = data['Price'] 
            left_stock =data['Stock']
        try: 
            int(quantity)
            if int(left_stock) < int(quantity): 
                return -2 #error 2: not enough stock 
            else:
                left_stock = int(left_stock) - int(quantity)
        except: 
            return -3 #error 3: error quantities
        #check product_id is in User_Api.total_cart
        if len(User_Api.total_cart) != 0:
            for i in range(len(User_Api.total_cart)):
                if User_Api.total_cart[i]['Product_id'] == product_id:
                    User_Api.total_cart[i]['Quantity'] = int(User_Api.total_cart[i]['Quantity']) + int(quantity)
                    User_Api.total_cart[i]['Price'] = int(User_Api.total_cart[i]['Price']) + int(quantity) * int(product_price)
                    if int(left_stock) < User_Api.total_cart[i]['Quantity']: 
                        return -2 #error 2: not enough stock 
                    else:
                        left_stock = int(left_stock) - int(quantity) 
                    User_Api.temp = User_Api.total_cart[i]['Price']
                    return -4 #error 4: product already in cart 

            self.cart = {}
            self.cart['Product_id'] = product_id 
            self.cart['Product_name'] = product_name
            self.cart['Quantity'] = quantity
            self.cart['Price'] = int(product_price) * int(quantity)
            User_Api.total_cart.append(self.cart)

            return self.cart

        else:   
            self.cart = {}
            self.cart['Product_id'] = product_id 
            self.cart['Product_name'] = product_name
            self.cart['Quantity'] = quantity
            self.cart['Price'] = int(product_price) * int(quantity)

            #add cart to cart.json in Data folder 
            User_Api.total_cart.append(self.cart)

            return self.cart

    #process 
    def process_cart(self): 
        self.create_new_invoice_id() 
        self.create_new_invoice({'Invoice_Id': self.new_invoice_id, 'InvoiceDate': datetime.datetime.now(), 'Total_Price': 0})
        for cart in User_Api.total_cart: 
            self.total_price = self.total_price + cart['Price'] 
        
        final = {}
        final['Invoice_Id'] = self.new_invoice_id 
        final['InvoiceDate'] = datetime.datetime.now()
        final['Cart'] = User_Api.total_cart
        final['TotalAmount'] = self.total_price

        self.create_new_invoice(final) 
        User_Api.total_cart = []
        return 0 #success


    # get all warehouse data by function get_all_warehouse_data
    # get all invoice data by function get_all_invoice_data