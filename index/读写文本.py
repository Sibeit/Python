import myComputer
a=open("名单.txt","wt")
i=1
while True:
    print("请输入第", i, "个学生信息")
    s=myComputer.write()
    a.write(s["No"]+"\n"+s["Name"]+"\n"+s["Gender"]+"\n"+s["Age"]+"\n")
    if input("输入任意继续，输入1显示")!=str(1):
        i+=1
    else:
        a.close()
        b = open("名单.txt", "rt")
        j=0
        while True:
            j+=1
            no=b.readline(j).strip()
            if no=="":
                break
            name=b.readline(j+1).strip()
            gender=b.readline(j+2).strip()
            age = b.readline(j+3).strip()
            print(no,name,gender)
        break
