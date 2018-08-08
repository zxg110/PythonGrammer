#通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的.
#如果我们不一定用到所有的元素，那么创建列表，就浪费了，既然列表是通过某种算法推算出来
#那我可以保存这种算法，用算法一边循环一边算，用多少算出来多少
#在Python中，这种一边循环一边计算的机制，称为生成器：generator
#要创建一个generator，有很多种方法。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator
#列表生成式：生成的是列表
L = [x * x for x in range(10)]

#生成器
g = (x * x for x in range(10))
#拿到生成器，可以通过next(g)来不断获取元素
next(g)
#我们讲过，generator保存的是算法，每次调用next(g)，就计算出g的下一个元素的值，直到计算到最后一个元素，
# 没有更多的元素时，抛出StopIteration的错误。我们也可以通过for循环获取元素，生成器也是可迭代的
for n in g:
    print(n)

#第二种方法
#在函数中使用关键字yield，这个函数就是生成器。
#函数打印斐波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

#生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

# 最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
# 而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句
# 处继续执行。

#举个简单例子：
def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield 3
    print('step 3')
    yield 5

o = odd()
next(o)
#step 1
#1
next(o)
#step 2
#3
next(o)
#step 3
#5
#next(o)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration

# 可以看到，odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。
# 执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。

#同样，用函数改造的generator，也基本不用next()获取，同样通过for
for n in fib(6):
    print("fib",n)
# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中，如下：

g = fib(6)
while True:
    try:
        x = next(g)
        print('fib',x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break


    def triangles1():
        # 初始化输出数组
        myList = [1]
        # 定义临时数组
        tempList = []
        while True:
            # 输出第一行数组
            yield myList
            # 在输出数组后添加一项。
            myList.append(0)
            # 遍历添加新数组内容
            for x in range(len(myList)):
                # 每次append之后，myList数组都会有变化
                tempList.append(myList[x - 1] + myList[x])
                # 将临时数组中的内容赋值给输出数据
                myList = tempList
                # 临时数组清空,为下一次存储做准备。
                tempList = []


    n = 0
    for t in triangles1():
        print(t)
        n = n + 1
        if n == 10:
            break

#使用生成器输出杨辉三角形
def triangles(n):
    list = [1]
    temp = []
    for x in range(n):
        yield list
        list.append(0)
        for i in range(len(list)):
            print('index',i)
            temp.append(list[i+1]+list[i])
            list = temp;
            print('after add',list)
            temp = []

g = triangles(4)
for x in g:
    print('triangles',x)

