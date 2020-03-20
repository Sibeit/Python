import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return 0

    def __str__(self):
        return str((self.x, self.y))


class Circle(Point):

    def __init__(self,x,y,radius):
        self.radius = int(radius)
        super().__init__(x,y)

    def area(self):
        super().area()
        return  self.radius* self.radius*math.pi

    def getArea(self):
        return  self.radius* self.radius*math.pi

    def perimeter(self):

        return  self.radius * 2 * math.pi

    def __str__(self):
        return "面积为" + str(self.area()) + "周长为" + str(self.perimeter())


class Cylinder(Circle):

    def __init__(self,x,y,radius,height):
        self.height = int(height)
        super().__init__(x, y,radius)


    def area(self):
        super().area()
        return self.perimeter() * self.height

    def volume(self):

        return self.getArea()*self.height

    def __str__(self):
        return "面积为" + str(self.area()) + "体积为" + str(self.volume())

a=Point(1,2)
b=Circle(1,2,3)
c=Cylinder(1,2,3,4)

print(a)
print(b)
print(c)


