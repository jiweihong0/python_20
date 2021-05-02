m=int(input("請輸入階層M:"))
n=a=1
while m>0:
    a=a*n
    if a>m:
        break
    n+=1
print("超過M為",m,"的最小階層N值為:",n)