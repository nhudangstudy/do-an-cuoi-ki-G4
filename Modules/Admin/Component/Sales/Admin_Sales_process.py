from tkinter import *
import Api.Admin_Api as Api


class Admin_Sales_Process: 
    @staticmethod
    def search_button_handle(obj):
        api = Api.Admin_Api()
        search = obj.searchentry.get()
        for i in obj.tree.get_children():
            obj.tree.delete(i)
        iv_id = api.invoices_collection.find({"Invoice_Id": search})
        # for row in iv_id:

    @staticmethod
    def visualize_button_handle(obj):
        pass
