shengfen=["江苏省","直辖市"]
city=[["常州市","徐州市","南京市","淮安市","南通市","宿迁市","无锡市","扬州市","盐城市","苏州市","泰州市","镇江市","连云港市"],["北京","上海","天津","重庆"]]
a=input("请输入查询地区")
for i in range(0,len(shengfen)):
    if shengfen[i]==a:
        b=1
        for j in range(0,len(city[i])):
            print(city[i][j],end=",")
        break
    else:
        b=0
if b==0:
    print("未找到")
