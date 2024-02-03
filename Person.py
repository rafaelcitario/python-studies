class Person:
    def __init__(self, name: str, age: int, mail: str, phone: str, id: str):
        self.name = name
        self.age = age
        self.mail = mail
        self.phone = phone
        self.id = id


    def display_person_info(self):
        print(f"Name: {self.name}".format(self.name))
        print(f"Age: {self.age}".format(self.age))
        print(f"Mail: {self.mail}".format(self.mail))
        print(f"Phone: {self.phone}".format(self.phone))
        print(f"Id: {self.id}".format(self.id))