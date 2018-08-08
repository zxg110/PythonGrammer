# Python内置的sorted()函数可以对list进行排序：
print(sorted([36, 5, -12, 9, -21]))
# 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
print(sorted([36, 5, -12, 9, -21],key=abs))

#给字串排序的例子：
sorted(['bob', 'about', 'Zoo', 'Credit'])
# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
# 现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，只要我们能用一个key函数把字符串映射为忽略大小写排序
# 即可。忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。
# 这样，我们给sorted传入key函数，即可实现忽略大小写的排序：
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
# ['about', 'bob', 'Credit', 'Zoo']

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
# ['Zoo', 'Credit', 'bob', 'about']

# exercise
#假设我们用一组tuple表示学生名字和成绩，请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]

print(sorted(L,key=by_name))