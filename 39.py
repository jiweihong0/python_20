n=int(input("請輸入一個奇數:"))
i=1
a=[]
s=''
for i in range(1,n//2+1):
    i=i*2-1
    print(" "*(n//2)+str(i))
for j in range(1,n//2+2):
    j=j*2-1
    a.append(j)
for k in a:
    s+=str(k)
x=len(a)-2
for r in range(len(a)-1):
    s+=str(a[x-r])
print(s)
for z in range(1,n//2+1):
    z=n-2*z
    print(" "*(n//2)+str(z))
