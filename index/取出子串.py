import myComputer
a=input("请输入字符串")
b=input("开始位置")
c=input("自串长度")
i=myComputer.takeout(a,b,c)
if i!=None:
    print("子串为",i)