#print方法，一个或多个字串，最后拼接输出
print("python","hello","world")

#读取键盘输入
#Python提供了两个内置函数从标准输入读入一行文本，默认的标准输入是键盘。如下：

# 1.raw_input函数 python没有了

#2.input
#input 可以接收一个Python表达式作为输入，并将运算结果返回。
#example:请输入：[x*5 for x in range(2,10,2)]
#你输入的是:  [10, 20, 30, 40]

#str = input("请输入：")
#print("你输入的是：",str)

#文件读写：
file = open("python_zxg.txt","w")
print("filename:",file.name)
file.write("www.runoob.com!\nVery good site!\n")
print("isClose:",file.closed)
print("mode:"+file.mode)
file.close()
print("isClose:",file.closed)

#用ab打开，append接着写
file = open("python_zxg.txt","ab")
file.write("hello world!\n".encode())
file.write(bytes("zxg\n",'utf-8'))
file.close()

#read
#read()方法从一个打开的文件中读取一个字符串。需要重点注意的是，Python字符串可以是二进制数据，而不是仅仅是文字。
#语法：fileObject.read([count]);
#被传递的参数是要从已打开文件中读取的字节计数。该方法从文件的开头开始读入，
# 如果没有传入count，它会尝试尽可能多地读取更多的内容，是直到文件的末尾。

file = open("python_zxg.txt","r+");
str = file.read();
print("read:",str);

#文件定位
#tell()方法告诉你文件内的当前位置；换句话说，下一次的读写会发生在文件开头这么多字节之后。
#seek（offset [,from]）方法改变当前文件的位置。Offset变量表示要移动的字节数。From变量指定开始移动字节的参考位置。
#打开模式一定要加上b，不然只能从开头开始读，不能位移
file = open("python_zxg.txt","rb+");
str = file.read(5);
print("read:",str);
position = file.tell();
print("position:",position);
file.seek(1,1)
print("continue read:",file.read(5))
file.close()

#重命名和删除文件
#Python的os模块提供了帮你执行文件处理操作的方法，比如重命名和删除文件。
#要使用这个模块，你必须先导入它，然后才可以调用相关的各种功能。

#rename 语法：os.rename(current_file_name, new_file_name)
import os
#os.rename("python_zxg.txt","zxg_python1.java")

#remove 语法：os.remove(file_name)
#若文件不存在，将报错
#os.remove("1.txt")

#Python里的目录：

#mkdir()方法
#可以使用os模块的mkdir()方法在当前目录下创建新的目录们。你需要提供一个包含了要创建的目录名称的参数。
#os.mkdir("newdir")

#getcwd()方法显示当前的工作目录。
cwd = os.getcwd()
print("current dir:",os.getcwd())

#chdir()方法 改变当前的目录。chdir()方法需要的一个参数是你想设成当前目录的目录名称。
# 将当前目录改为"/home/newdir"
os.chdir(cwd+"/newdir")
file = open("newFile.txt","w")
file.close()
os.remove(file.name)

os.chdir(cwd)

#rmdir()方法
#rmdir()方法删除目录，目录名称以参数传递。在删除这个目录之前，它的所有内容应该先被清除。
#并且需要离开该目录（当前目录不是要删除的目录）
os.rmdir(cwd+"/newdir")