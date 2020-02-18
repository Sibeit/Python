import openpyxl
import xlwt
class stus:

    def __init__(self,no,name,gender,age):
        self.no=no
        self.name=name
        self.gender=gender
        self.age=age

    def show(self):
        print(self.no, self.name, self.gender, self.age)

    def save(self):
        a=open("名单.txt","at")
        a.write(str(self.no)+"，"+str(self.name)+"，"+str(self.gender)+"，"+str(self.age)+"\n")
        a.close()



class stl:

    def __init__(self):
        self.sts=[]

    def show(self):
        print("学号",    "姓名",    "性别",    "年龄")
        for s in self.sts:
            s.show()

    def __insert(self,s):
        i=0
        while (i<len(self.sts) and s.no>self.sts[i].no):
            i+=1
        if (i<len(self.sts) and s.no==self.sts[i].no):
            print("已经存在")
        self.sts.insert(i,s)
        print("添加成功")

    def insert(self):
        while True:
            no = input("学号：")
            if no.isdecimal():
                no=int(no)
                break
            else:
                print("输入错误，请重输")
        while True:
            name = input("姓名：")
            if name!="":
                break
            else:
                print("不能为空，请重输")
        while True:
            gender=input("性别：")
            if gender=="男" or gender=="女":
                break
            else:
                print("输入错误，请重输")
        while True:
            age = input("年龄：")
            if age.isdecimal():
                age=int(age)
                break
            else:
                print("输入错误，请重输")
        self.__insert(stus(no,name,gender,age))

    def __update(self,s):
        flag=False
        for i in range(len(self.sts)):
            if s.no==self.sts[i].no:
                self.sts[i].name=s.name
                self.sts[i].gender=s.gender
                self.sts[i].age=s.age
                print("修改成功")
                flag=True
                break
        if flag==False:
            print("查无此人")

    def update(self):
        while True:
            no = input("学号：")
            if no.isdecimal():
                no = int(no)
                break
            else:
                print("输入错误，请重输")
        while True:
            name = input("姓名：")
            if name != "":
                break
            else:
                print("不能为空，请重输")
        while True:
            gender = input("性别：")
            if gender == "男" or gender == "女":
                break
            else:
                print("输入错误，请重输")
        while True:
            age = input("年龄：")
            if age.isdecimal():
                age = int(age)
                break
            else:
                print("输入错误，请重输")
        self.__update(stus(no,name,gender,age))

    def __delete(self,no):
        flag=False
        for i in range(len(self.sts)):
            if no==self.sts[i].no:
                del self.sts[i]
                print("删除成功")
                flag=True
                break
        if flag==False:
            print("查无此人")

    def delete(self):
        while True:
            no = input("学号：")
            if no.isdecimal():
                no = int(no)
                break
            else:
                print("输入错误，请重输")
        self.__delete(no)

    def save(self):
        for o in self.sts:
           o.save()
        print("保存成功")

    def load(self):
        b = open("名单.txt", "rt")
        while True:
            a=b.readline()
            if a=="":
                break
            print(a)
        print("读取完成")
        b.close()

    def write_excel_xls(self,path, sheet_name):
        index = len(self.sts)
        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet(sheet_name)
        for i in range(0, index):
            for j in range(0, len(self.sts[i])):
                sheet.write(i, j, self.sts[i][j])
        workbook.save(path)
        print("格式表格写入数据成功")

    def pro(self):
        while True:
            print("--------------------------------------------------------------------------------------------------")
            print("请输入序号，输入其他退出程序")
            print("1.显示     2.添加        3.更新        4.删除        5.保存至txt        6.从txt中读取")
            s=input(">")
            if s=="1":
                self.show()
            elif s=="2":
                self.insert()
            elif s=="3":
                self.update()
            elif s=="4":
                self.delete()
            elif s=="5":
                self.save()
            elif s=="6":
                self.load()
            else:
                break



st=stl()
st.pro()