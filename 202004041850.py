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
        return "姓名"+str(self.name)+"分数"+str(self.score)
class Sort(object):
    @staticmethod
    def List(list):
        n=len(list)
        for i in range(n-1):
            for j in range(n-i-1):
                if list[j] > list[j+1]:
                    k=list[j+1]
                    list[j+1]=list[j]
                    list[j]=k


stulist=[]
stulist.append(Student("reimu:",82))
stulist.append(Student("momiji",74))
stulist.append(Student("cirno",99))
Sort.List(stulist)
for i in stulist:
    print(i)