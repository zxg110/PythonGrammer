# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
def now():
    print('2017-12-27')


f = now;
f()

# 函数对象有一个__name__属性，可以拿到函数的名字：
print(now.__name__)
print(f.__name__)


# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，
# 称之为“装饰器”（Decorator）。

# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
    def wrapper1(*args, **kw):
        print('call of %s()', func.__name__)
        return func(*args, **kw)

    return wrapper1
#Tip: *args表示任何多个无名参数，它是一个tuple；**kwargs表示关键字参数，它是一个dict。并且同时使用*args和**kwargs时，必须*args参数列
# 要在**kwargs前

@log
def now(str):
    print('2017-12-27')


now(str)

# 把@log放到now()函数的定义处，相当于执行了语句：
log(now)

# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，
# 即在log()函数中返回的wrapper()函数。
# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，
# 再紧接着调用原始函数。

#如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
def log1(text):
    def decorator(fn):
        def wrapper(*args,**kw):
            print('%s %s():'%(text,fn.__name__))
            return fn(*args,**kw)
        return wrapper
    return decorator

@log1('excute')
def fn(x,y,z):
    return x+y+z

fn(1,2,3)
#相当于如下代码：
now = log('execute')(now)

# 我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。

####
# 我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名
# 的代码执行就会出错。不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，
# 所以，一个完整的decorator的写法如下：
import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


# 练习
# 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间：
import time



def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        ticks = time.time()
        print('start value', ticks)
        fn(*args, **kw)
        print('end value', time.time() - ticks)

    return wrapper


@metric
def fast(x, y):
    time.sleep(2)
    return x + y


fast(1, 2)
