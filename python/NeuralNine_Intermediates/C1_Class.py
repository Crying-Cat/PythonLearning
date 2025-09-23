import copy

class Person:
    # 静态变量
    className = "Person"
    amount = 0
    def __init__(self,name="undefined",age=12): #构造函数
        self.name = name #成员变量
        self.age = age #成员变量
        print("A person has been created.")
        Person.amount += 1
    def __del__(self): #析构函数
        print(f"{self.name} has been deleted.")
        Person.amount -= 1
    def __str__(self): #print调用的函数
        return f"Person(name={self.name}, age={self.age})"
    def talk(self): #成员函数
        print(f"My name is {self.name} and I am {self.age} years old.")

if __name__ == "__main__":
    p1 = Person("Alice", 30)
    p1.talk()
    p2 = Person("Mike", 19)
    p2.talk()

    #copy&deepcopy
    p3 = p2 #copy (shallow copy)
    p3.name = "John"
    p2.talk()
    p4 = copy.deepcopy(p2) #deepcopy (complete copy)
    p4.name = "Bob"
    p2.talk()

    #print objects
    print(p1)

    #静态变量
    print(Person.className)

    input("Press Enter to delete persons...")