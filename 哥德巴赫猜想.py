i=int(2)
b=int(2)
x=int(1)
t=int(0)
while t==0:
    try:
        m = int(input("请输入一个数值"))
        if m>=6 and m%2==0:
            while t<m:
                for x in range(x+1,m):
                    for i in range(2,x+1):
                        if x%i==0:
                            break
                    if x==i:
                        a=i
                        break
                j=int(m-a)
                while b<j :
                    if j%b!=0:
                        b=b+1
                    else:
                        break
                if b==j:
                    print(a,"+",b)
                else:
                    t=t+1
        else:
            print("请输入6以上偶数")
    except Exception as err:
        print("请输入有效整数")