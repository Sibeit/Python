'''
@Author: your name
@Date: 2020-03-24 13:18:52
@LastEditTime: 2020-03-28 13:35:16
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Python\202003241318.py
'''
class Employee(object):
    def __init__(self,n):
        self.__name=n
    def getSalary(self):
        pass
class Manager(Employee):
    def __init__(self,n):
        super().__init__(n)
    def getSalary(self):
        return 12000
class Programmer(Employee):
    def __init__(self,n,h):
        self.__workhours=h
        super().__init__(n)
    def getSalary(self):
        return 200*self.__workhours
class Salesman(Employee):
    def __init__(self,n,s):
        self.__sales=s
        super().__init__(n)
    def getSalary(self):
        return 1800+self.__sales*0.05
class Checker(object):
    def judge(self,job):
        return job.getSalary()

i={"aya":"Salesman","satori":"Manager","cirno":"Programmer","kaguya":"Programmer","momiji":"Salesman","junko":"Manager"}
j=Checker()
for key in i:
    if i[key] == "Manager":
        print("Name:", key,"\nJob:Manager\nSalary:", j.judge(Manager(key)))
    elif i[key] == "Salesman":
        print("Please enter",key,"'s sales:")
        s = int(input())
        print("Name:", key,"\nJob:Salesman\nSalary:", j.judge(Salesman(key, s)))
    elif i[key] == "Programmer":
        print("Please enter",key,"'s working hours:")
        h = int(input())
        print("Name:", key,"\nJob:Programmer\nSalary:", j.judge(Programmer(key, h)))
    else:
        print("error")


