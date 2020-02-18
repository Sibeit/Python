class date:
    __month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    def __init__(self,y,m,d):
        if y<=0:
            raise Exception("无效年份")
        if m<1 or m>12:
            raise Exception("无效月份")
        if y%400==0 or y%4==0  and y%100!=0:
            date.__month[2]=29
        if d>date.__month[m] or d<1:
            raise Exception("无效日期")
        self.year=y
        self.month=m
        self.day=d
    def show(self):
            print(self.year,"年",self.month,"月",self.day,"日")
try:
    a=int(input("年份："))
    b=int(input("月份："))
    c=int(input("日期："))
    d=date(a,b,c)
    d.show()
except Exception as e:
    print(e)