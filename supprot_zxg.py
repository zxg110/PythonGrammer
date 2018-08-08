# 自定义模块，其他py文件可以通过以下方式应用：
# 全部引用:import support 或 from support_zxg import *
# 引用某个函数：from supprot_zxg import print_fun
def print_fun(str):
    print("zxg supprot"+str);
    return