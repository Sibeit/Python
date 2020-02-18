class book:
    def __init__(self,ISBN,Title,Author,Publishers):
        self.ISBN=ISBN
        self.Title=Title
        self.Author=Author
        self.Publishers=Publishers

    def show(self):
        print(self.ISBN,self.Title,self.Author,self.Publishers)

    def save(self):
        a=open("书单.txt","wt")
        a.write(str(self.ISBN)+"，"+str(self.Title)+"，"+str(self.Author)+"，"+str(self.Publishers)+"\n")
        a.close()
class booklist:
    def __init__(self):
        self.bl=[]

    def show(self):
        print("书号","标题","作者","出版商")
        for i in self.bl:
            i.show()

    def __insert(self, s):
        i = 0
        while (i < len(self.bl) and s.ISBN > self.bl[i].ISBN):
            i+=1
        if (i < len(self.bl) and s.ISBN == self.students[i].ISBN):
            print(s.ISBN + "已经存在")
        self.bl.insert(i, s)
        print("添加成功")

    def insert(self):
        while True:
            ISBN = input("版号：")
            if ISBN.isdecimal():
                ISBN = int(ISBN)
                break
            else:
                print("输入错误，请重输")
        while True:
            Title = input("书名：")
            if Title!= "":
                break
            else:
                print("不能为空，请重输")
        while True:
            Author = input("作者：")
            if Author != "":
                break
            else:
                print("不能为空，请重输")
        while True:
            Publishers = input("出版社：")
            if Publishers != "":
                break
            else:
                print("不能为空，请重输")
        self.__insert(book(ISBN, Title, Author, Publishers))

    def __update(self, s):
        flag = False
        for i in range(len(self.bl)):
            if s.ISBN == self.bl[i].ISBN:
                self.bl[i].Title = s.Title
                self.bl[i].Author = s.Author
                self.bl[i].Publishers = s.Publishers
                print("修改成功")
                flag = True
                break
        if flag == False:
            print("查无此书")

    def update(self):
        while True:
            ISBN = input("版号：")
            if ISBN.isdecimal():
                ISBN = int(ISBN)
                break
            else:
                print("输入错误，请重输")
        while True:
            Title = input("书名：")
            if Title != "":
                break
            else:
                print("不能为空，请重输")
        while True:
            Author = input("作者：")
            if Author != "":
                break
            else:
                print("不能为空，请重输")
        while True:
            Publishers = input("出版社：")
            if Publishers != "":
                break
            else:
                print("不能为空，请重输")
        self.__update(book(ISBN, Title, Author, Publishers))

    def __delete(self, ISBN):
        flag = False
        for i in range(len(self.bl)):
            if ISBN == self.bl[i].ISBN:
                del self.bl[i]
                print("删除成功")
                flag = True
                break
        if flag == False:
            print("查无此书")

    def delete(self):
        while True:
            ISBN = input("版号：")
            if ISBN.isdecimal():
                no = int(ISBN)
                break
            else:
                print("输入错误，请重输")
        self.__delete(ISBN)

    def save(self):
        for o in self.bl:
            o.save()
        print("保存成功")

    def load(self):
        b = open("书单.txt", "rt")
        while True:
            a = b.readline()
            if a == "":
                break
            print(a)
        print("读取完成")
        b.close()

    def start(self):
        while True:
            print(
                "--------------------------------------------------------------------------------------------------")
            print("请输入序号，输入其他退出程序")
            print("1.显示教材   2.添加教材   3.更新教材    4.删除教材    5.保存    6.读取")
            s = input(">")
            if s == "1":
                self.show()
            elif s == "2":
                self.insert()
            elif s == "3":
                self.update()
            elif s == "4":
                self.delete()
            elif s == "5":
                self.save()
            elif s == "6":
                self.load()
            else:
                break

st=booklist()
st.start()