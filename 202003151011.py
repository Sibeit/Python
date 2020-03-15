class Dog:

    def __init__(self,no,ad_no,vgrade,date):
        self.__no=  no
        self.__ad_no = ad_no
        self.__vgrade = vgrade
        self.__date = date

    def show(self):
        self.info = Info(self.__no, self.__ad_no, self.__vgrade, self.__date)

class Cat:

    def __init__(self,no,ad_no,vgrade,date):
        self.__no=  no
        self.__ad_no = ad_no
        self.__vgrade = vgrade
        self.__date = date
        self.info = Info(self.__no, self.__ad_no, self.__vgrade, self.__date)

    def show(self):
        self.info = Info(self.__no, self.__ad_no, self.__vgrade, self.__date)

class Info:

    def __init__(self,no,ad_no,vgrade,date):
        self.__no = no
        self.__ad_no = ad_no
        self.__vgrade = int(vgrade)
        if self.__vgrade == 1:
            self.__level = "特级会员"
        elif self.__vgrade == 2:
            self.__level = "高级会员"
        else:
            self.__level = "普通会员"
        self.__date = date

    def show(self):
        print("当前宠物信息为:\n编号为：",self.__no,"\n管理员编号为：",self.__ad_no,"\nvip等级为：",self.__level,"\n入会日期为：",self.__date,"\n")


dog1=Dog("dog1","001","2","20200315")
dog1.show()
dog1.info.show()
cat1=Cat("cat1","002","1","20200314")
cat1.show()
cat1.info.show()