class Book():
    def __init__(self, arg_list):
        self.user_name = arg_list["name"]
        self.password = arg_list["password"]
        self.id_number = arg_list["id"]
    def Show_Column(self):
        return {
            "id": self.id_number,
            "passowd": self.password,
            "name": self.user_name,
        }
    def Add_Column(self, visa_mode):
        return visa_mode
    def Rem_Column(self, visa_mode):
        return visa_mode
