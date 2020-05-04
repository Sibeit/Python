def gbs(a,b):#最小公倍数
    i = a
    if a < b:
        i = b
    for j in range(i,a*b+1):
        if j%a == 0 and j%b == 0:
            break
    return j
def gys(a,b):#最大公因数
    i = a
    if a>b:
        i = b
    while i >= 1:
        if a%i == 0 and b%i == 0:
            break
        else:
            i = i-1
    return i
def zs(a):#判断质数
    for i in range(2,a+1):
        if a%i == 0:
            break
    if a == i:
        j = 0
    else:
        j = 1
    return j
def nx(a):#逆向输出字符
    t=""
    j=int(len(a))
    for i in range(j-1,-1,-1):
        t=t+a[i]
    return (t)
    '''for i in range(0,j):
        t=t+a[-i-1]
    return (t)
    '''
def despace(a):#除左右空格
    t=""
    i=0
    j=len(a)-1
    while i<=j and a[i]==" ":
        i=i+1
    while i<=j and a[j]==" ":
        j=j-1
    for b in range(i,j+1):
        t=t+a[b]
    return t
def xxturn(a):#小写转大写
    t=""
    for i in range(0,len(a)):
        if a[i]>="a" and a[i]<="z":
            t=t+chr(ord("A")+ord(a[i])-ord("a"))
        else:
            t=t+a[i]
    return t
def dxturn(a):#大写转小写
    t = ""
    for i in range(0, len(a)):
        if a[i] >= "A" and a[i] <= "Z":
            t = t + chr(ord("a") + ord(a[i]) - ord("A"))
        else:
            t = t + a[i]
    return t
def symmetry(a):#判断对称
    t=""
    for i in range(len(a)-1,-1,-1):
        t=t+a[i]
    if a==t:
        return 1
    else:
        return 0
def takeout(a,b,c):#从a字符串取出从位置b开始长度为c的子串
    t = ""
    l=int(b+c)
    if len(a)<l:
        print("溢出")
    else:
        for i in range(int(b)-1,int(c)+1):
            t=t+a[i]
        return t
def findstr(a,b):#在a字符串中查找b出现的位置
    t = ""
    for i in range(0,len(a)):
        if a[i]==b:
            t=t+str(i+1)+","
    return t
def strcut(a,b):#在a字符串查找b
    i=len(a)
    j=len(b)
    for z in range(0,i,j):
        if a[z:z+j]==b:
            y=True
            break
        else:
            y=False
    return y
def max(*args):
    j=args[0]
    for i in range (len(args)):
        if j<args[i]:
            j=args[i]
    return j
def postion(a,b):
    j = []
    for i in range(0,len(a)):
        if a[i]==b:
          j.append(i+1)
    return j
def city(a):
    city={"广东":["广州","深圳"],"四川":["成都","乐山"]}
    if a in city.keys():
        print(a,"的城市有",city[a])
    else:
        print("数据库中无此省份")
words=[{"word":"about","note":"在附近，关于"},{"word":"post","note":"邮寄"}]
def show():
    for l in words:
        print(l["word"],l["note"])
    print()

def enter():
    w={}
    w["word"]=input("单词")
    w["note"]=input("翻译")
    return w

def find(a):
    i=0
    j=len(words)-1
    while i<=j:
        m=(i+j)//2
        if words[m]["word"]==a:
            print(words[m]["word"],words[m]["note"])
            return
        elif words[m]["word"] > a:
            j=m-1
        else:
            i=m+1
    print("查找失败")

def insert(a):
    i = 0
    j = len(words) - 1
    while i <= j:
        m = (i + j) // 2
        if words[m]["word"] == a["word"]:
            print(m["word"],"已经存在")
            return
        elif words[m]["word"] > a["word"]:
            j = m - 1
        else:
            i = m + 1
    words.insert(i,a)
    print("添加成功")

def update(a):
    i = 0
    j = len(words) - 1
    while i <= j:
        m = (i + j) // 2
        if  words[m]["word"] == a["word"]:
            words[m]["note"]=a["note"]
            print("更新成功")
            return
        elif words[m]["word"] > a["word"]:
            j = m - 1
        else:
            i = m + 1
    print("未找到")

def delete(a):
    i = 0
    j = len(words) - 1
    while i <= j:
        m = (i + j) // 2
        if words[m]["word"] == a:
            del words[m]
            print("删除成功")
            return
        elif words[m]["word"] > a:
            j = m - 1
        else:
            i = m + 1
    print("未找到")
def write():

    while True:
        no = input("No=")
        if no.isdecimal():
            break
        else:
            print("输入错误，请重输")
    while True:
        name = input("Name=")
        if name != "":
            break
        else:
            print("不能为空，请重输")
    while True:
        gender = input("Gender=")
        if gender == "男" or gender == "女":
            break
        else:
            print("输入错误，请重输")
    while True:
        age = input("Age=")
        if age.isdecimal():
            break
        else:
            print("输入错误，请重输")
    s={}
    s["No"]=no
    s["Name"]=name
    s["Gender"]=gender
    s["Age"]=age
    return s