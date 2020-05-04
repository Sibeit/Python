m=int(input("请输入范围"))
i=int(2)
x=int(2)
j=int(0)
for x in range(2,m):
    for i in range(2,x+1):
        if x%i== 0 :
            break
    if x==i:
        print(i,end=",")
        j=j+1
print(j)

