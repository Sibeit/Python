'''
@Author: Sibeit
@Date: 2020-04-04 18:49:35
@LastEditTime: 2020-04-04 22:24:14
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Python\202004041850.py
'''
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def __eq__(self,other):
        if self.name==other.name and self.score==other.score:
            return True
        else:
            return False
    def __gt__(self,other):
        if self.score>other.score:
            return True
    def __str__(self):
        return "姓名："+str(self.name)+"分数："+str(self.score)
class Sort(object):
    @staticmethod
    def List(list):
        n=len(list)
        for i in range(n-1):
            for j in range(n-i-1):
                if list[j] < list[j+1]:
                    k=list[j+1]
                    list[j+1]=list[j]
                    list[j]=k


stulist=[]
stulist.append(Student("reimu",69))
stulist.append(Student("momiji",74))
stulist.append(Student("cirno",99))
stulist.append(Student("koishi",51))


Sort.List(stulist)
for i in stulist:
    print(i)

print("————————————————————————————————————")
print("删除学生koishi")
print("————————————————————————————————————")

for j in range(len(stulist)):
    if stulist[j]==Student("koishi",51):
        del stulist[j]
for i in stulist:
    print(i)
