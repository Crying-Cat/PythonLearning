from abc import ABC,abstractmethod

#1.接口不能实例化
#2.接口的方法必须被实现
class IPerson(ABC): #接口
    @abstractmethod
    def person_method(self):
        """abstractmethod"""
    @staticmethod
    @abstractmethod
    def class_method():
        """abstractmethod"""

class Student(IPerson):
    def __init__(self):
        pass
    def person_method(self):
        print("I am a student")
    @staticmethod
    def class_method():
        print("Student class")
        
class Teacher(IPerson):
    def __init__(self):
        pass
    def person_method(self):
        print("I am a teacher")
    @staticmethod
    def class_method():
        print("Teacher class")

s = Student()
s.person_method()
Student.class_method()

t = Teacher()
t.person_method()
Teacher.class_method()