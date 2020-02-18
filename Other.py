import random
j=random.randint(1,20)
k=0
while k<5:
    i=int(input("猜数"))
    if i<j:
        print("猜小了")
    elif i>j:
        print("猜大了")
    else:
        print("猜中了")
        break
    k+=1