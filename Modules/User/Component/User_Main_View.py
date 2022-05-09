from tkinter import *

class User_Main_View:

    def __init__(self):
        self.window = Tk()

        # get screen width and height
        self.screen_width = self.window.winfo_screenwidth()
        self.screen_height = self.window.winfo_screenheight()

        # set window width and height
        self.window_width = 1080
        self.window_height = 720
        
        # set window position
        self.window.geometry("%dx%d+%d+%d" % (self.window_width, self.window_height,
                             (self.screen_width - self.window_width) / 2, (self.screen_height - self.window_height) / 2))

        self.window.title("User")
        self.window.configure(bg = "#AFA4F9")
        self.window.iconphoto(False, PhotoImage(file = f"./Images/User/UserIcon.png"))

        self.canvas = Canvas(self.window, bg = "#FFFFFF", height = 720, width = 1080, bd = 0, highlightthickness = 0, relief = "ridge")
        self.canvas.place(x = 0, y = 0)

        self.background_img = PhotoImage(file = f"./Images/User/BG_MainPage.png")
        self.background = self.canvas.create_image(540, 360, image=self.background_img)




app = User_Main_View()
app.window.mainloop()