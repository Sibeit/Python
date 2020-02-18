class Student:
    def __init__(self,No,Name,Gender,Age):
        if No.isdigit():
            self.No = No
        else:
            raise Exception('无效学号')
        if Gender!='男' and Gender!='女':
            raise Exception('性别输入错误')
        if Age.isdigit():
            self.Age = int(Age)
        else:
            raise Exception('无效年龄')
        self.Name = Name
        self.Gender = Gender


    def show(self):
        print('%-16s %-16s %-10s %-10d' %(self.No ,self.Name, self.Gender,self.Age))

class St:
    def __init__(self):
        self.students = []

    def show(self):
        print('%-16s%-16s%-9s%-9s'%("学号", '姓名', '性别','年龄'))
        for s in self.students:
            s.show()

    def __insert(self,s):
        i=0
        while (i<len(self.students) and s.No>self.students[i].No):
            i=i+1
        if (i<len(self.students) and s.No == self.students[i].No):
            print(s.No + "已经存在")
            return  False
        self.students.insert(i,s)
        print("增加成功")


    def __update(self,s):
        flag = False
        for i in range (len(self.students)):
            if (s.No == self.students[i].No):
                self.students[i].Name = s.Name
                self.students[i].Gender= s.Gender
                self.students[i].Age = s.Age
                print("修改成功")
                flag = True
                break
        if (not flag):
            print("没有这个学生")

    def __delete(self,No):
        flag = False
        for i in range(len(self.students)):
            if (self.students[i].No == No):
                del self.students[i]
                flag = True
                print("删除成功")
                break
        if (not flag):
            print("没有这个学生")



    def delete(self):
        while True:
            No=input('No=')
            if (No != '' and No.isdigit()):
                self.__delete(No)
                break
            else:
                print('请输入删除的学号')

    def insert(self):
        No = input('No=')
        Name = input("Name=")
        while True:
            Gender = input("Gender=")
            if (Gender == '男' or Gender=='女'):
                break
            else:
                print("Gender is not valid")
        Age = input('Age=')

        if No!='' and Name!='':
            self.__insert(Student(No,Name,Gender,Age))
        else:
            print('学号,姓名不能为空')

    def update(self):
        while True:
            No = input('No=')
            if (No != '' and  No.isdigit()):
                No = No
                break
            else:
                print('请输人正确的学号')
        Name = input("Name=")
        while True:
            Gender = input("Gender=")
            if (Gender=='男' or Gender=='女'):
                break
            else:
                print("性别输入错误")

        Age = input('Age=')
        if Name != '':
            self.__update(Student(No, Name, Gender, Age))
        else:
            print('姓名不能为空')


    def Go(self):
        print('----------------------------------学生信息管理-------------------------------------')
        print('显示:show    ,插入:insert    ,修改:update      ,删除:delete       ,退出:exit')
        try:
            while True:
                s = input('>')
                if s == 'show':
                    self.show()
                elif s == 'insert':
                    self.insert()

                elif s == 'update':
                    self.update()

                elif s == 'delete':
                    self.delete()

                elif s == 'exit':
                    print('程序结束')
                    break
                else:
                    print('请输入正确的函数:')
        except Exception as err:
            print(err)

K=St()
K.Go()
