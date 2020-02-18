#创建列表
list1=[1,5,19,114,514]
print(list1)

#访问列表值
print("list1[0]:",list1[0])
print("list1[1:3]:",list1[1:3])

#修改列表项
list1[1]="b"

#删除列表项
del list1[2]

#联合列表
list2=["qwer",21,1919,810]
list3=list1+list2
#列表截取
list1[2:4:1]#start:stop:step

#判断列表是否包含某元素
a=(114 in list1)#布尔值

#常用操作函数
list1.append("aaa")#在列表末尾添加元素

list1.count("aaa")#统计元素在列表中出现次数

list1.extend(list2[2:3])#在列表末尾添加令一列表多个值

list1.index("aaa")#查找某值第一个匹配项的位置，没有会报错

list1.insert(2,"aaa")#在第a项插入b

list1.remove("aaa")#移除某值第一个匹配项，没有会报错

list1.pop(2)#弹出某个项，默认值为-1，即最后一项

list1.reverse()#将元素反向排列

list1.sort()#将元素进行大小排序，所有元素必须是同一类，否则报错