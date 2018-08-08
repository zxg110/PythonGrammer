class Animal:
    'base animal'
    animalCount = 0;

    #定义构造方法
    def __init__(self,name,level):
        self.name = name;
        self.level = level
        Animal.animalCount +=1

#析构函数 __del__ ，__del__在对象销毁的时候被调用，当对象不再被使用时，__del__方法运行
    def __del__(self):
        class_name = self.__class__.__name__


    def displayCount(self):
        print ("Total Animal %d",Animal.animalCount);

    def displayAnimal(self):
        print("animal name:",self.name,"level:",self.level)





animal1 = Animal("dog",1);
animal1.displayAnimal()
animal2 = Animal("cat",2);

#可以添加、修改、删除对象属性
animal1.age = 2; #添加
animal1.age = 3; #修改
print("animal1.age",animal1.age);
del animal1.age #删除

#打印这句会报错，由此理解增加的是对象的属性，并不是类
#print("animal2.age",animal2.age);

# 你也可以使用以下函数的方式来访问属性：
# getattr(obj, name[, default]) : 访问对象的属性。
# hasattr(obj,name) : 检查是否存在一个属性。
# setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
# delattr(obj, name) : 删除属性。
print("getattr:",getattr(animal1,'level'))
print("hasattr:",hasattr(animal1,"age"))
setattr(animal2,"age",25)
print("animal2.age",animal2.age);
delattr(animal2,"age")

# Python内置类属性
# __dict__ : 类的属性（包含一个字典，由类的数据属性组成）
# __doc__ :类的文档字符串
# __name__: 类名
# __module__: 类定义所在的模块（类的全名是'__main__.className'，如果类位于一个导入模块mymod中，那么className.__module__ 等于 mymod）
# __bases__ : 类的所有父类构成元素（包含了一个由所有父类组成的元组）
print("dict",Animal.__dict__);
print("doc",Animal.__doc__);
print("Class name:",Animal.__name__)
print("module:",Animal.__module__)
print("bases:",Animal.__bases__)


def print():
    print("124")