from tkinter import *
import Modules.Login.Login_View as lgv
# import User.Items_View as uiv
# import User.Shopnow_View as usv

class User_process:
    @staticmethod 
    def log_out_button_handle(obj): 
        obj.window.destroy() 
        app = lgv.Login_View() 
        app.window.mainloop()

    # @staticmethod
    # def items_button_handle(obj):
    #     obj.window.destroy()
    #     app = uiv.Items_View()
    #     app.window.mainloop()

    # @staticmethod
    # def shopnow_button_handle(obj):
    #     obj.window.destroy()
    #     app = usv.Shopnow_View()
    #     app.window.mainloop()


