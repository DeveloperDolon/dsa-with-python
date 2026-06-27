class BaseClass:
    def __init__(self, name, age):
        self.name = name;
        self.age = age;
    
    def info(self):
        return f"User name: {self.name} and age: {self.age}";


class AdminUser(BaseClass):
    def __init__(self, name, age, role):
        super().__init__(name, age)
        self.role = role;
    
    def displayRole(self):
        return f"The role is : {self.role}";

