import math
a=float(input("请输入a"))
b=float(input("请输入b"))
c=float(input("请输入c"))
if (b*b-(4*a*c))>=0:
    i= math.sqrt(b*b-(4*a*c))
    print("结果为:x1=",(-b+i)/(2*a),"x2=",(-b-i)/(2*a))
else:
    print("错误")

a=input("a")
a=int(a)
print(a)