class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score
    def __eq__(self,other)
        if self.name==other.name and self.score==other.score:
            return True
        else:
            return False
    def __gt__(self,other):
        if self.score>other.score:
            return True
class Sort(object):
    @staticmethod
    def List(list)
        n=len(list)
            while n>0:
                for i in range(n-1):
                    if list[i] > list[i+1]:
                    list[i], list[i+1] = list[i+1], list[i] 
                n-=1

stulist=[]
stulist.append(Student(reimu,82))
stulist.append(Student(momiji,74))
stulist.append(Student(cirno,99))
Sort.list(stulist)
for i in stulist:
    print(i)