class Person:
    def __init__(self,n,g,a,w,h):
        if g!="男" and g!="女"or a< 0 or w< 0 or h< 0:
            raise Exception("无效输入")
        self.name=n
        self.gender=g
        self.age=a
        self.weight=w
        self.height=h
    def introduce(self):
        print("我叫",self.name,",性别",self.gender,",身高",self.height,",体重",self
              .weight)
    def bmi(self):
        bmi=self.weight/(self.height*2)
        if bmi<18.5:
            return "过轻"
        elif bmi>=18.5 and bmi<23.9:
            return "正常"
        elif bmi>=24 and bmi<27:
            return "过重"
        elif bmi>28 and bmi<=32:
            return "肥胖"
        else:
            return "非常肥胖"
try:
    n=input("请输入姓名：")
    g=input("请输入性别：")
    a=int(input("请输入年龄："))
    w=int(input("请输入体重："))
    h=int(input("请输入身高："))
    i=Person(n,g,a,w,h)
    i.introduce()
    print(i.bmi())
except:
    print("输入错误")