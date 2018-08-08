from OOP import Animal


class Dog(Animal.Animal):
    def __init__(self, name, level, age):
        #调用父类的构造函数写法
        Animal.__init__(name,level)
        self.age = age


dog = Dog('tom',1,23)
print("Dog age:",dog.age,"Dog name:",dog.name)
print(type(dog))
