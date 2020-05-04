def max (a,b):
    if len(a) >= len(b):
        j = int(len(a))
    elif len(a) < len(b):
        j = int(len(b))
    for i in range(0, j):
        if a[i] != b[i]:
            if a[i] > b[i]:
                z = 1
                break
            else:
                z = 2
                break
        else:
            z = 0
    return z
p=input("请输入第一串")
q=input("请输入第二串")
y=max(p,q)
if y==0:
    print("相等")
elif y==1:
    print("1>2")
else:
    print("1<2")