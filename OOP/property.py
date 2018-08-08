#在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
class Student(object):
    __slots__ = 'source'

s = Student()
s.source = 9999

# 这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，
# 在set_score()方法里，就可以检查参数：

class Student(object):
    def get_source(self):
        return self._source

    def set_source(self,value):
        if not isinstance(value,int):
            raise ValueError('source must be an integer')
        if value > 100 or value <0:
            raise ValueError('source must between 0~100')
        self._source = value


s = Student()
#ok
s.set_source(60)
#crash
#s.set_source(999)

#上面的调用方法又略显复杂，没有直接用属性这么直接简单。Python内置的@property装饰器就是负责把一个方法变成属性调用的：
class Student(object):
    @property
    def source(self):
        return self._source

    @source.setter
    def source(self,value):
        if not isinstance(value,int):
            raise ValueError('source must be an integer')
        if value > 100 or value <0:
            raise ValueError('source must between 0~100')
        self._source = value

s = Student()
s.source=60 #实际上转化为s.set_source(60)
s.source #实际上转化为s.get_source
print('source',s.source)

# 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
class Student(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

s = Student()
# s.age = 12 #crash can't set attribute