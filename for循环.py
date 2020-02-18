j=int(0)
k=int(0)
a=int(0)
while a<=0 or a>=10 or n<=0:
    a = int(input("请输入a"))
    n = int(input("请输入n"))
for i in range(n):
     j=10*j+a
     k=j+k
     if i<n-1:
         print(j,end="+")
     else:
         print(j,end="=")
print(k)
