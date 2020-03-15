import math
class point:
    count=0

    def __init__(self,x,y):
        self.__x=x
        self.__y=y
        point.count+=1

    def move(self):
        self.x = self.__x
        self.y = self.__y
        self.x += self.__x
        self.y += self.__y
        return (self.x,self.y)

    def distance(self):
        return  math.sqrt(self.__x^2+self.y^2)

    def toString(self):
        return (self.__x,self.__y)

i=point(1,2)
print(i.toString())
print(i.move())
print(i.distance())


