from tkinter import *
import Api.Admin_Api as Api
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns 
class Admin_Sales_Process: 
    @staticmethod
    def search_button_handle(obj):
        api = Api.Admin_Api()
        search = obj.searchentry.get()

        for i in obj.tree.get_children():
            obj.tree.delete(i)
        data = api.get_all_invoices_data()
        for row in data: 
            if search in row["Invoice_Id"]:
                obj.tree.insert("", "end", values=(row["Invoice_Id"], row["InvoiceDate"], row["Product_id"], row["Product_name"], row["Quantity"], row["Price"]))

    @staticmethod
    def visualize_button_handle(obj):
        api = Api.Admin_Api() 
        invoices = api.invoices_collection.find()
        date = []
        total_price = [] 
        for row in invoices: 
            date.append(row["InvoiceDate"].date())
            total_price.append(row["TotalAmount"])

        if len(date) > 30:
            date = date[-30:] 
            total_price = total_price[-30:] 

        sns.set(style="darkgrid") 
        plt.figure(figsize=(12, 6))
        sns.lineplot(date, total_price) 
        plt.xlabel("Date")
        plt.ylabel("Total Price") 
        plt.show() 
    

        


