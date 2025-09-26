class Person():
    __instance = None
    def __init__(self,name,age):
        if Person.__instance is not None: ##避免重复创建
            raise Exception("单例被重复创建")
        self.name = name
        self.age = age
        Person.__instance = self #给单例赋值
        super().__init__()
    def __str__(self):
        return f"name:{self.name} age:{self.age}"
    @staticmethod
    def getInstacne():
        if Person.__instance is None:
            Person("wyj",12)
        return Person.__instance
    
print(Person.getInstacne())
try:
    Person('wyj',12)
except Exception as e:
    print(e)

input("按任意键结束")