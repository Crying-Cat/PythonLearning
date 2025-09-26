class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    
    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,value):
        self.__name = value

    @staticmethod
    def say():
        print("Hello world")

p = Person('wyj',25)
p.Name = 'yyl'
print(p.Name)

Person.say()