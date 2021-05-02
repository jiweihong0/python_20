l1=[]
l2=[]
n = int(input("輸入筆數n："))
for i in range (n):
    a,b=input("").split(" ")
    l1.append(a)
    l2.append(b)
for j in range(len(l1)):
    print(str(l1[j])+"牌得到"+str(l2[j])+"面")