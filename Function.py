#函数
def power(x):
    return x*x;
print(power(4));
#Python中函数也是一个对象,可以赋值,可以拷贝,可以像普通变量那样使用.其实可以理解为C语言中的指针:
def includePower(i,x):
    return x(i);
print(includePower(4,power))

#匿名函数,或者叫做lambda函数,它没有名字,只有参数和表达式:
d = lambda x:x*x;
#lambda最大的用处是用作实参:
def iter(func,args):
    ret = [];
    for var in args:
        ret.append(func(var));
    return ret;
print("lambda:",iter(lambda x:x*2,list_b))

#一些常用的内置函数
#len()---返回列表,字串的长度
#range([start], stop, [step]) --- 生成一个整数列表,从,start开始,到stop结束,以step为步长
#help(func)---获取某个函数的帮助文档.

import subprocess;
#subprocess.call(["ls", "-l"])
