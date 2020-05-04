'''
@Author: your name
@Date: 2020-05-04 20:29:06
@LastEditTime: 2020-05-04 21:55:05
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Python\202005042029.PY
'''
try:
    b = open("test.txt", "rt")
    li=[]
    while True:
        nu=b.readline().strip("\n")
        print(nu)
        if nu=="":
            b.close
            break
        li.append(nu)
except IOError as e:
    print(e)
j=0
l=len(li)
for i in range(0,l):
    try:
        li[i]=float(li[i])
    except TypeError as e:
        print(e)
        l-=1
        continue
    except IndexError as e:
        print(e)
        l-=1
        continue
    except ValueError as e:
        print(e)
        l-=1
        continue
    j=j+li[i]
print(j)
print("平均值为",j/l)


    
