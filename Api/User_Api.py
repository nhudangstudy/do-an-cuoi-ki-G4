import Main_Api as main_api 
import json
import datetime 
class User_Api(main_api.Api): 
    def __init__(self): 
        super().__init__() 
        self.connector() 
        self.total_cart = []
    
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
        self.cursor = self.warehouse_collection.find({'Product_Name': product_name})
        if self.cursor == None: 
            return -1 #error 1: product is not exist 
        else: 
            self.product = self.cursor[0] 
            self.product_id = self.product['Product_Id'] 
            self.product_name = self.product['Product_Name']
            self.product_price = self.product['Product_Price'] 
            self.left_stock = self.product['Stock_Stock']

            if self.left_stock < quantity: 
                return -1 #error 1: not enough stock 
            else:
                self.left_stock = self.left_stock - quantity 

            #create cart.json file in Data folder
            self.cart = {}
            self.cart['Product_Id'] = self.product_id 
            self.cart['Product_Name'] = self.product_name
            self.cart['Quantity'] = quantity
            self.cart['Price'] = self.product_price * quantity
 
            #add cart to cart.json in Data folder 
            self.total_cart.append(self.cart)

            return 0 #success 

    #process 
    def process_cart(self): 
        self.create_new_invoice_id() 
        self.create_new_invoice({'Invoice_Id': self.new_invoice_id, 'InvoiceDate': datetime.datetime.now(), 'Total_Price': 0})
        for cart in self.total_cart: 
            self.total_price = self.total_price + cart['Price'] 
        
        final = {}
        final['Invoice_Id'] = self.new_invoice_id 
        final['InvoiceDate'] = datetime.datetime.now()
        final['Cart'] = self.total_cart
        final['TotalAmount'] = self.total_price

        self.create_new_invoice(final) 
        self.total_cart = []
        return 0 #success


    # get all warehouse data by function get_all_warehouse_data
    # get all invoice data by function get_all_invoice_data