class Book():
    def __init__(self, user_name, password, id_number):
        self.user_name = user_name
        self.password = password
        self.id_number = id_number
    def Show_Column(self):
        return {"id": self.id_number,
                "passowd": self.password,
                "name": self.user_name}
    def Add_Column(self, visa_mode):
        return visa_mode
    def Rem_Column(self, visa_mode):
        return visa_mode
