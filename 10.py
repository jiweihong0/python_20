nm=input("輸入N及M為:").split()
n=[]

for i in range(int(nm[0])):
    n.append(input("輸入矩陣數值第%d列為:"%(i+1)).split())
m=list(zip(*n))
for j in range(int(nm[1])):
    print("輸出矩陣數值第%d列為:%s"%(j+1,m[j])) 