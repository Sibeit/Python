import myComputer
flag=0
while flag==0:
    print("1.显示 2.查找 3.增加 4.更新 5.删除 6.退出")
    s=int(input("请选择"))
    if s==1:
        myComputer.show()
    elif s==2:
        a=input("要查找的单词")
        myComputer.find(a)
    elif s==3:
        a=myComputer.enter()
        myComputer.insert(a)
    elif s==4:
        a=myComputer.enter()
        myComputer.update(a)
    elif s==5:
        a=input("输入要删除的单词")
        myComputer.delete(a)
    else:
        flag=1