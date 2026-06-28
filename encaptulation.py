class AIEngineer: 
    def __init__(self, name, age, experience):
        self.__name__ = name;
        self.__age__ = age;
        self.__experience__ = experience;

    @property
    def Name(self): 
        return self.__name__;

    @Name.setter
    def Name(self, value):
        self.__name__ = value;

    @staticmethod
    def myStaticMethod():
        print('Static method calling!');

en1 = AIEngineer("Dolon Roy", 24, 2.5);

print(en1.Name);

en1.Name = 'Roy';

print(en1.Name);