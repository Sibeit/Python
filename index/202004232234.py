'''
@Author: your name
@Date: 2020-04-23 22:34:53
@LastEditTime: 2020-04-24 00:21:51
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Python\202004232234.py
'''
def test(li):
    try:
        n1=int(li[0])
        n2=int(li[1])
        res = n1/n2
        print(res)
    except TypeError as e:
        print(e)
    except IndexError as e:
        print(e)
    except ValueError as e:
        print(e)
    except ZeroDivisionError as e:
        print(e)
    else:
        print("运算正常")

b = open("test.txt", "rt")
i=[]
while True:
    nu=b.readline().strip("\n")
    print(nu)
    if nu=="":
        b.close
        break
    i.append(nu)
test(i)