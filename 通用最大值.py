import myComputer
a="y"
j=[]
x=0
while a=="y" :
    i=int(input("输入一个数字"))
    j.append(i)
    a=input("输入y继续，输入其他结束")
for z in range (len(j)):
    if x<j[z]:
        x=j[z]
print("最大值为",x)

