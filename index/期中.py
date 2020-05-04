import myComputer
print("1.求最小公倍数    2.求最大公倍数" )
print("3.判断是否为质数    4.退出程序" )
t = int(input("请选择一项"))
if t == 1:
    print("请输入两个数")
    a = int(input("请输入第1个数"))
    b = int(input("请输入第2个数"))
    i = myComputer.gbs(a,b)
    print(a,",",b,"的最小公倍数为",i)
elif t == 2:
    print("请输入两个数")
    a = int(input("请输入第1个数"))
    b = int(input("请输入第2个数"))
    i = myComputer.gys(a,b)
    print(a,",",b,"的最大公因数",i)
elif t == 3:
    a = int(input("请输入要判断的数"))
    i = myComputer.zs(a)
    if i == 0:
        print(a,"是质数")
    else:
        print(a, "不是质数")
else:
    print("程序结束")