#列表生成式即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
#生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[range(1,11)]

#生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环
L = []
for x in range(1, 11):
    L.append(x * x)

#方法2
[x*x for x in range(1,11)]
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#还可带判断条件
list1 = [x*x for x in range(1,11) if x%2==0]

# 还可以使用两层循环，可以生成全排列：
[m + n for m in 'ABC' for n in 'XYZ']
#['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

#运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现
import os
print('dir',[d for d in os.listdir('.')])

#将一个非法的list中单词变成小写
L = ['Hello', 'World', 18, 'Apple', None]
newL = [x.lower() for x in L if isinstance(x, str)]
print('newL:', newL)
