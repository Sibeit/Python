class Date:
    __month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    def __init__(self,y,m,d):
        if y<=0:
            raise Exception("无效年份")
        if m<1 or m>12:
            raise Exception("无效月份")
        if y%400==0 or y%4==0  and y%100!=0:
            Date.__month[2]=29
        if d>Date.__month[m] or d<1:
            raise Exception("无效日期")
        self.year=y
        self.month=m
        self.day=d
    def show(self,end="\n"):
        print(self.year,"年",self.month,"月",self.day,"日",end=end)
class Datetime:
    def __init__(self,y,m,d,h,mi,s):
        Date.__init__(self,y,m,d)
        if h>=24 or h<0 or mi>=60 or mi<0 or s>=60 or s<0:
            raise Exception("无效时间")
        self.hour=h
        self.min=mi
        self.sec=s
    def show(self):
        Date.show(self,end=" ")
        print(self.hour,"时",self.min,"分",self.sec,"秒")
try:
    a=int(input("年份："))
    b=int(input("月份："))
    c=int(input("日期："))
    d=int(input("小时："))
    e=int(input("分钟："))
    f=int(input("秒："))
    l=Datetime(a,b,c,d,e,f)
    l.show()
except Exception as e:
    print(e)