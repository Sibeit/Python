i=int(1)
while i<=3:
    pw=input("请输入密码")
    if pw==str(123):
        print("正确")
        break
    else:
        print("错误")
        i=i+1