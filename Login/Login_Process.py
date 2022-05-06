import Api.Api as Api
from tkinter import messagebox
import Signup.Sign_up_View as suv


class Login_Process:
    @staticmethod
    def confirm_button_handle(obj):
        username = obj.name_entry.get()
        password = obj.password_entry.get()
        print(username, password)
        api = Api.Api()
        c = api.check_user_login(username, password)
        if c == -1:
            messagebox.showerror("Warning", "Invalid User Input")
        elif c == -2:
            messagebox.showerror("Warning", "User not found")
        elif c == -3:
            messagebox.showerror("Warning", "Wrong password")
        else:
            if c == "Admin":
                messagebox.showinfo("MB", "Welcome Admin")
            if c == "User":
                messagebox.showinfo("MB", "Welcome User")


    @staticmethod 
    def signup_button_handle(obj):
        obj.window.destroy()
        app = suv.Sign_up_View()
        app.window.mainloop()


