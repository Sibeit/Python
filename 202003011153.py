class Rect():

    def __init__(self):
        self.__length=0
        self.__width=0

    def setlength(self,l):
        if l < 0:
            raise Exception("输入错误")
        else:
            self.__length=l

    def getlength(self):
        return self.__length

    def setwidth(self,h):
        if h <0:
            raise Exception("输入错误")
        else:
            self.__width=h

    def getwidth(self, ):
        return self.__width

    def tostring(self):
        print("长:",self.__length,"宽：",self.__width)

    def area(self):
        print("面积为",self.__length*self.__width)

    def perimeter(self,):
        print("周长为",self.__length*2+self.__width*2)

try:

    i=int(input("输入长："))
    j=int(input("输入宽："))
    r=Rect()
    r.setlength(i)
    r.setwidth(j)
    r.tostring()
    r.perimeter()
    r.area()

except Exception as e:
    print(e)

