n=int(input("輸入第一行正整數"))
m=input("第二行中數列中的數字為:").split()
mset=set(m)
nm=list(mset)
a={}
for i in range(len(nm)):
    a[nm[i]]=0
    for j in range(len(m)):
        if nm[i]==m[j]:
            a[nm[i]] += 1
for k in a:
    if a[k]>=2:
        print("最大出現數的數字為:",k)
        print("出現次數為:",a[k])
if len(m)==len(mset):
    print("每個數字剛好出現一次")
