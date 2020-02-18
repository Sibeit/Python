a=int(input("请输入第一个数"))
b=int(input("请输入第二个数"))
if b>=a:
    i=b
    j=a
else:
    i=a
    j=b
k=i
while k<=i:
    if i%k==0 and j%k==0:
        break
    else:
        k=k-1
print("最大公约数是",k)
h=int((i*j)/k)
print("最小公倍数是",h)
