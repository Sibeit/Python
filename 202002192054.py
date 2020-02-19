import math
class Circle:
    def __init__(self,r):
        if r<0:
            raise Exception("无效半径")
        self.radius=r
    def area(self):
        a=math.pi*self.radius*self.radius
        return a
    def perimeter(self):
        c=2*math.pi*self.radius
        return c
r=int(input("请输入圆的半径"))
i=Circle(r)
print("周长为","%.2f"%i.perimeter(),"半径为""%.2f"%i.area())