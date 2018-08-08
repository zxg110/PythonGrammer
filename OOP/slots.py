#当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，
# 这就是动态语言的灵活性。先定义class：

class Student(object):
    pass

#动态绑定属性
s = Student()
s.name = 'tom'

#动态绑定方法
def set_age(self,age):
    self.age = age

from types import MethodType
s.setage = MethodType(set_age,s) #方法名可以不一样
s.setage(25)
print('age:',s.age)

#但是，给一个实例绑定的方法，另一个实例是无法拥有的，那么我们可以给类绑定方法
def set_source(self,source):
    self.source = source
Student.set_source = set_source

#通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上
# 功能，这在静态语言中很难实现。

# 使用__slots__
#
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该
# class实例能添加的属性：

class emplty(object):
    __slots__ = ('name','age')

#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的，如下
class Subempty1(emplty):
    pass

#合法，只能定义name age的限制不起作用了
sube = Subempty1()
sube.source = 70
print('source',sube.source)



#除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。
#个人理解子类定义了__slots__，就会继承父类的__slots

class Subempty2(emplty):
    __slots__ = 'source'

sube2 = Subempty2()
#Subempty2限制了只能绑定属性source，但是这里也可以绑定父类限制的属性name：
sube2.name = 'tom'
print('name',sube2.name)