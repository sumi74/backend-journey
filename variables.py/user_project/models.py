class user:
    def __init__(self, name, email, city):
        self.name = name
        self.email = email
        self.city = city

    def show_info(self):
        print("name:", self.name)
        print("email:", self.email)
        print("city:", self.city)

        