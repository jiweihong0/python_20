n=input("輸入一整數續列為:").split()
m=set(n)
k=list(m)
dir1 = {}

for x in range(len(k)): 
    dir1[k[x]] = 0
    for y in range(len(n)):
        if k[x] == n[y]:
            dir1[k[x]] += 1
for i in dir1:
    if dir1[i]>=len(n)//2:
        print("過半元素:",i)
