import Api.Main_Api as main_api 

class Admin_Api(main_api.Api): 
    def __init__(self): 
        super().__init__() 
        self.connector() 
    