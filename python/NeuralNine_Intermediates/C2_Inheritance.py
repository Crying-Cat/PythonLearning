class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
    def get_older(self, years):
        self.age += years

class Worker(Person):#继承Person类
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary
    def __str__(self): 
        return f"Person(name={self.name}, age={self.age}, salary={self.salary})"
    def calc_yearly_salary(self):
        return self.salary*12


wyj = Worker("wyj",12,23)
print(wyj)