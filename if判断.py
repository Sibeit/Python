import  math
i=input("请输入一个年份")
i=float(i)
if (i%4==0 and 0 != i%100) or i//400==0 :
    print(i,"是闰年")
else:
    print("不是闰年")


mat=input("请输入数学成绩")
en=input("请输入英语成绩")
zh=input("请输入语文成绩")
mat=float (mat)
en=float(en)
zh=float(zh)
j=((mat+en+zh)/3)
print("平均分为",j,"分")


num=input("请输入一个数")
num=float (num)
if num%2==0:
        print("是偶数")
else:
    print("是奇数")

a=input("请输入一个字符")
if a<="z" and a>="a":
    print(a,"是一个小写字母")
elif a<="Z" and a>="A":
    print(a,"是一个大写字母")
elif a<="9" and a>="0":
    print(a,"是一个数字")
