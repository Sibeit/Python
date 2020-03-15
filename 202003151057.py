class Point:

    def __init__(self,x,y):
        self.__x=x
        self.__y=y

    def move(self,x,y):
        self.__x+=x
        self.__y+=y
        return self

    def __str__(self):
        return str((self.__x,self.__y))

class Circle:

    def __init__(self,r, x, y):
        self.p=Point(x,y)
        self.radius=r

    def __str__(self):
        return "圆心:"+str(c.p)+"半径:"+str(self.radius)


c=Circle(10,1,2)
print(c)
c.p.move(2,3)
print(c)