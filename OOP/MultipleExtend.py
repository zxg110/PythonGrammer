#Python允许多重继承
class Animal(object):
    pass

# 大类:
#哺乳动物
class Mammal(Animal):
    pass
#鸟类动物
class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass
#蝙蝠
class Bat(Mammal):
    pass
#鹦鹉
class Parrot(Bird):
    pass
#鸵鸟
class Ostrich(Bird):
    pass

#现在，我们要给动物再加上Runnable和Flyable的功能，只需要先定义好Runnable和Flyable的类：
class Runnable(object):
    def run(self):
        print('running...')

class Flyable(object):
    def fly(self):
        print('flying')

#对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog：
class Dog(Mammal,Runnable):
    pass
d = Dog()
d.run()
#通过多重继承，一个子类就可以同时获得多个父类的所有功能。

# MixIn
#
# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，通过多重继承就可以实现，比如，
# 让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
#
# 为了更好地看出继承关系，我们把Runnable和Flyable改为RunnableMixIn和FlyableMixIn。类似的，你还可以定义出肉食动物CarnivorousMixIn
# 和植食动物HerbivoresMixIn，让某个动物同时拥有好几个MixIn：

class RunnableMaxIn(object):
    def run(self):
        print('running...')

class FlyableMaxIn(object):
    def fly(self):
        print('flying')

class Bat(Mammal,RunnableMaxIn):
    pass

