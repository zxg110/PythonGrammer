#Dictionary字典
#相当于Java中的HashMap,用于以Key/Value方式存储的容器.创建方式为{key1: value1, key2: value2, ....},
# 更改方式为dict[key] = new_value；索引方式为dict[key]. dict.keys()方法以List形式返回容器中所有的Key；
# dict.values()以List方式返回容器中的所有的Value:
#创建字典
box = {'fruits':["apple","orange"],'time':1993,'name':"tom"}
box_1 = dict(name="top",age="22") #注意：key键不能用引号，不能写'name'='tom'
box_2 = dict(zip(['name','age'],['tom',22]))
print (box);
box['id'] = "01"
print(box)

#modify
box['name'] = "jery"
print(box['name'])
print(box.keys())
print(box.values())
#返回字典 d 中键 x 对应的值，若键 x 不存在，则返回
# y， 并将 x : y 作为键值对添加到字典中，y 的默认值为 None
box.setdefault('nam1','no name')
print("set default",box)

#将字典 d2 所有键值对添加到字典 d1 中(不重复，重复的键值对用字典 x 中的键值对替代字典 d 中)
d1 = dict(x=1,y=2)
d2 = dict(x=2,z=3)
d1.update(d2)
print("update d1:",d1)

