class car:
    count=0
    manufacturer=""
    model=""

    def __init__(self,n,s):
        self.__number=n
        self.__speed=s
        car.count+=1

    def addspeed(self):
        self.__speed+=20
        return self.__speed

p=car(111,10)
i=p.addspeed()
print(i)
print(car.count)
q=car(222,20)
p.addspeed()
j=p.addspeed()
print(j)
print(car.count)

