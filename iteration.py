# 如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
# 在Python中，迭代是通过for ... in来完成的，而很多语言比如C语言，迭代list是通过下标完成的，比如Java代码：
# for (i=0; i<list.length; i++) {
#     n = list[i];
# }

# Python的for循环抽象程度要高于C的for循环，因为Python的for循环不仅可以用在list或tuple上，
# 还可以作用在其他可迭代对象上。list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，
# 但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.values()，如果要同时迭代key和value
# 可以用for k, v in d.items()。

for value in d.values():
    print(value)

for k,v in d.items():
    print("key",k,"value",v)

#在Python中，只要是一个可迭代对象，我们都可使用for进行迭代，那么如何判断一个对象是否为可迭代的呢？
#方法是通过collections模块的Iterable类型判断：
from collections import Iterable
isinstance('abc',Iterable) # str是否可迭代
isinstance([1,2,3], Iterable) # list是否可迭代
isinstance(123,Iterable) # 整数是否可迭代

#如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list
# 变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：

for i,value in enumerate(['a','b','c']):
    print(i,value)

#请使用迭代查找一个list中最小和最大值，并返回一个tuple：
def findMinAndMax(L):
    if not isinstance(L,list):
        print("data error")
        return
    if len(L) == 0:
        return (None,None)

    max = L[0]
    min = L[0]
    if len(L) == 1:
        return (max,min)

    for value in L:
        if value > max:
            max = value
        if value < min:
            min = value
    return (max,min)

print("max min:",(findMinAndMax([-1,2,3,4,-5])))

