class MyDate:

    __m = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self):
        self.__year = 0
        self.__month = 0
        self.__day = 0

    def setYear(self, y):
        self.__year = y

    def getYear(self):
        return self.__year

    def setMonth(self, m):
        if 1 <= m <= 12:
            self.__month = m
        else:
            raise Exception("输入错误")

    def getMonth(self):
        return self.__month

    def setDay(self, d):
        if self.__year % 400 == 0 or self.__year % 4 == 0 and self.__year % 100 != 0 :
            MyDate.__m[2]=29
        if d>MyDate.__m[self.__month] or d<1:
            raise Exception("输入错误")
        else:
            self.__day=d

    def toString(self):
        print(self.__year, "年", self.__month, "月", self.__day, "日")

try:

    i = int(input("输入年份："))
    j = int(input("输入月份："))
    k = int(input("输入日期："))
    date=MyDate()
    date.setYear(i)
    date.setMonth(j)
    date.setDay(k)
    date.toString()

except Exception as e:

    print(e)
