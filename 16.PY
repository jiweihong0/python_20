n= input().split()
n1=[]
for i in range(int(n[0])):
    n2=input().split()
    n1.append(n2)
m= input().split()
m1=[]
for j in range(int(m[0])):
    m2=input().split()
    m1.append(m2)
print(n1,m1)
ans=[]
for k in range(int(n[0])):
    for l in range(int(n[0])):
        if len(m1)==len(n1) and len(m1[0])==len(n1[0]):
            ans1=int(n1[k][l])+int(m1[k][l])
            ans.append(str(ans1))
ans2=' '
ans3=[]
for p in range(len(ans)):
    if (p+1)%2==0:
        ans3.append(str(ans[p])+"\n")
    else:
        ans3.append(ans[p])
print(ans3)
for o in ans3:
    ans2+=str(o)+" "
print(ans2)
  