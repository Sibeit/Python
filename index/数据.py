a=input("请输入一个数")
a=int(a)
i=int(2)
while i<a:
    if a%i!=0:
        i=i+1
    else:
        break
if a==i:
    print(a,"是质数")
else:
    print(a,"不是质数")