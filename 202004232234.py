'''
@Author: your name
@Date: 2020-04-23 22:34:53
@LastEditTime: 2020-04-23 23:36:51
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \Python\202004232234.py
'''
def test(li):
    try:
        n1=li[0]
        n2=li[1]
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
        print("正常运行")


a=int(input("第一个数："))
b=int(input("第二个数："))
test([a,b])