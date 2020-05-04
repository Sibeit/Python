'''
@Author: Sibiet
@Date: 2020-04-04 21:04:46
@LastEditTime: 2020-04-04 21:46:19
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Python\202004042104.py
'''
import math
class Point(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        x=self.x + other.x
        y=self.y + other.y
        return (x,y)
        
    def __eq__(self,other):
        if self.x==other.x and self.y==other.y:
            return True
        else:
            return False
    def __ne__(self,other):
        if self.x==other.x and self.y==other.y:
            return False
        else:
            return True
    def __gt__(self,other):
        a=math.sqrt(self.x^2+self.y^2)
        b=math.sqrt(other.x^2+other.y^2)
        if a>b:
            return True
        else:
            return False
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"

a=Point(3,2)
b=Point(1,4)
print("输出点a,b:",a,b)
print("两点相加：",a+b)
print("判断是否重叠：",a==b)
print("判断是否不重叠：",a!=b)
print("判断a是否大于b：",a>b)
