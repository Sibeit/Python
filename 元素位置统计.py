import myComputer
a=[]
b="y"
while b!="n":
    i=input("输入要添加的元素")
    a.append(i)
    b=input("输入任意继续，n结束")
print("查询列表为",a)
c=input("要查询的元素")
print("出现位置为",myComputer.postion(a,c))