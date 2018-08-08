from supprot_zxg import print_fun
from math import *

counter = 100  # 整型变量
miles = 1000.0  # 浮点型变量
name = "runoob"  # 字符串

print(counter)
print(miles)
print(name)

# list:
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1)
print(list_1[2])
# 越界
# print (list_1[3])
# 切片操作
# list[start:end] --- 返回从start开始,到end-1,也就是list[start], list[start+1].....list[end-1]
# 取0,1,2
print(list_1[0:3])

# list[start:end:step] --- 与上面类似,只不过每隔step取一个
print(list_1[0:8:2])
# list[:end]  ---- 缺省的开端是
print(list_1[:6])

# 负数索引，倒数切片，记住倒数第一个元素的索引是-1
print(list_1[-1])
# result:10

#所有数，每5个取一个
list_1[::5]

print_fun("test str")

# list inner mothod

# inclusion relation: in  not in
print(3 in list_1)  # True
print(3 not in list_1)  # False

# connector:+
print(list_1 + [20, 21])  # [1,2,...10,20,21]

list_2 = list_1 + [20, 21]
# repetition
print(list_2 * 2)  # [1,2,...10,1,2...10]

# Tuple not variable:
tuple = (1, 2, 3)
print(tuple)

#String 字符串就是一个字符的数组,List的操作都可以对String直接使用.
str = "hello,python"
print(str[0:3])
print("ello" in str)

#字串格式化符% 这是一个类似C语言printf和Java中的String.format()的操作符,它能格式化字串,整数,浮点等类型:语句是:
print("int:%d,float:%f,string:'%s'"%(5,2.3,"hello"))




#query
# print("box size",len(box)) #query size
# print("box keys:",box.keys()) #query keys
# print("box value:",box.values()) #query values
# print("box items",box.items()) #query values
# list_3 = list(box.items())
# print("set box.item to list",list_3[1])
# print("query whether have key","name" in box) #query whether have the key True
# print("query value by key with defalut",box.get("name1","nothing"));




# #迭代字典的方法
# for k,v in box.items():
#     print('k,v:%s,%s'%(k,v))
#
# #delete
# del box['name'] # 删除键是'name'的条目
# #box.pop('name') # 删除键是'name'的条目
# box.clear() #清空词典所有条目
# del box # 删除词典


#分支语句
a = 3;
b = 4;
c = 5;
if( b>a or c>b):
    print("1")
elif (a<b and c>b):
    print("2")
else:
    print("3")

#while循环
i = 0;
while i<6:
    print("i:",i);
    i += 1;

#for语句
msg = "hello";
for a in msg:
    print (a)

#列表推导式
#[expr for value in collection ifcondition]
#相当于
#result = []
# value in collection:
#    if condition:
#        result.append(expression)

#example过滤掉长度小于3的字符串列表，并将剩下的转换成大写字母
names = ['Bonb','Tom','alice','wendy','smith']
names1 = [name.upper() for name in names if len(name) >3]
print("after condition",names1)

#遍历列表a,对其是偶数的项,乘方.
list_a = range(8);
list_b = [x*x for x in list_a if x%2 == 0]
print("list b:",list_b)


#while
numbers = [12,11,23,43,2,4,5,6,67]
event = []
odd = []
while len(numbers):
    number = numbers.pop()
    if(number % 2 == 0):
        event.append(number)
    else:
        odd.append(number)

friuts = ["apple","banana","orange","mango"]
for index in range(len(friuts)):
    print("当前水果：",friuts[index]);

#使用嵌套循环输出2~100之间的素数
# i = 2;
#
# while (i < 100):
#     j = 2;
#     while (j <= (i / j)):
#         if not (i % j):
#             break;
#         j = j + 1;
#         if (j > i / j):
#             print(i, "素数")
#         i = i + 1;


#tuple

L = [['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']]
print("apple",L[1][1])

Name = ['adam', 'LISA', 'barT']

def normalize(name):
    return name.capitalize()

lizeName = list(map(normalize,Name))
print("after lize:",lizeName)

from functools import reduce


def prod(L):
    return reduce(lambda x,y:x*y,L)

number = [1,3,5,4]
print("prod:",prod(number))

def test(n1,n2):
    return n1*n2



CHAR_TO_FLOAT = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    ".":-1
}

def str2float(s):
    nums = map(lambda ch: CHAR_TO_FLOAT[ch], s)
    point = 0
    def to_float(f, n):
        print("f,n",f,n)
        nonlocal point
        if n == -1:
            point = 1
            return f
        if point == 0:
            return f * 10 + n
        else:
            point = point * 10
            return f + n / point
    return reduce(to_float, nums, 0.0)

print(str2float('123.456'))

L = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print('L',L)