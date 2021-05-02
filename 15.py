
d=input("輸入一組四位數字為:")
a=[]
for i in d:
    num=(int(i)+7)%10
    a.append(num)
print("輸出加密後的數字為:%d%d%d%d" %(a[2],a[3],a[0],a[1]))