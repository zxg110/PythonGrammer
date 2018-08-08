class people:
    # 定义基本属性
    name = '';
    age = 0;
    # 定义私有属性，外部无法直接访问
    __weight = 0

    # 定义构造方法
    def __init__(self, name, age, weight):
        self.name = name;
        self.age = age;
        self.__weight = weight;

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 单继承示例
class student(people):
    grade = 0;

    def __init__(self, name, age, weight, grade):
        people.__init__(self, name, age, weight)
        self.grade = grade

    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级" % (self.name, self.age, self.grade))


class speaker():
    topic = '';
    name=''

    def __init__(self,name,topic):
        self.name = name;
        self.topic = topic;

    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s" % (self.name, self.topic))

#多重继承
class studentspeaker(speaker,student):
    def __init__(self,name,age,weight,grade,topic):
        student.__init__(self,name,age,weight,grade)
        speaker.__init__(self,name,topic)

test = studentspeaker('Tim','25','80','1','python');
test.speak()  #方法名同，默认调用的是在括号中排前地父类的方法

# 类属性与方法
# 类的私有属性
# __private_attrs：两个下划线开头，声明该属性为私有，不能在类地外部被使用或直接访问。
# 在类内部的方法中使用时 self.__private_attrs。
# 类的方法
# 在类地内部，使用 def 关键字来定义一个方法，与一般函数定义不同，类方法必须包含参数 self，
# 且为第一个参数，self 代表的是类的实例。
# self 的名字并不是规定死的，也可以使用 this，但是最好还是按照约定是用 self。
# 类的私有方法
# __private_method：两个下划线开头，声明该方法为私有方法，只能在类的内部调用 ，
# 不能在类地外部调用。self.__private_methods。

#私有变量test
class JustCounter:
    __secretCount = 0  # 私有变量
    publicCount = 0  # 公开变量

    def count(self):
        self.__secretCount += 1
        self.publicCount += 1
        print(self.__secretCount)


counter = JustCounter()
counter.count()
counter.count()
print(counter.publicCount)
#print(counter.__secretCount)  # 报错，实例不能访问私有变量


class Site:
    def __init__(self, name, url):
        self.name = name  # public
        self.__url = url  # private

    def who(self):
        print('name  : ', self.name)
        print('url : ', self.__url)

    def __foo(self):  # 私有方法
        print('这是私有方法')

    def foo(self):  # 公共方法
        print('这是公共方法')
        self.__foo()


x = Site('菜鸟教程', 'www.runoob.com')
x.who()  # 正常输出
x.foo()  # 正常输出
x.__foo()  # 报错

#运算符重载
#Python同样支持运算符重载，我们可以对类的专有方法进行重载，实例如下：

class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    #可以理解为类似于toString
    def __str__(self):
        return 'Vector (%d, %d)' % (self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)


v1 = Vector(2, 10)
v2 = Vector(5, -2)
print(v1 + v2)

#执行结果：Vector(7,8)