from tkinter import * 
import Login.Login_View as lgv 

class Admin_Process: 
    @staticmethod 
    def log_out_button_handle(obj): 
        obj.window.destroy() 
        app = lgv.Login_View() 
        app.window.mainloop()
