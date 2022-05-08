from tkinter import * 
import Modules.Login.Login_View as lgv
# import Modules.Admin.Products_View as productsview
# import Modules.Admin.Inventory_View as inventoryview
# import Modules.Admin.Sales_View as salesview
# import Modules.Admin.User_View as userview

class Admin_Process: 
    @staticmethod 
    def log_out_button_handle(obj): 
        obj.window.destroy() 
        app = lgv.Login_View() 
        app.window.mainloop()

    # @staticmethod 
    # def products_button_handle(obj): 
    #     obj.window.destroy() 
    #     app = productsview.Products_View()
    #     app.window.mainloop()

    # @staticmethod
    # def inventory_button_handle(obj):
    #     obj.window.destroy() 
    #     app = inventoryview.Inventory_View() 
    #     app.window.mainloop()

    # @staticmethod
    # def sales_button_handle(obj):
    #     obj.window.destroy() 
    #     app = salesview.Sales_View()
    #     app.window.mainloop()

    # @staticmethod
    # def user_button_handle(obj):
    #     obj.window.destroy() 
    #     app = userview.User_View()
    #     app.window.mainloop()