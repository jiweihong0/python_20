a1=[]
for i in range(10):
    a=input("請輸入第%d個數字" %(i+1))
    a1.append(a)
a1.sort()    
print("最大的3個數字"+a1[9]+","+a1[8]+","+a1[7])
print("最小的3個數字"+a1[2]+","+a1[1]+","+a1[0])
