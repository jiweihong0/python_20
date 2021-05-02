a=input("請輸入正整數:")
a1=[]
a2=[]
for i in range(len (a)):
    for y in range(len (a)+1):
        a1.append(a[i:y])
a1=[x for x in a1 if x!='']
for k in range(len(a1)):
    for c in range(2,int(a1[k])):
        if int(a1[k]) % c == 0:
            break    
        elif c == int(a1[k])-1:
            a2.append(a1[k])
    if int(a1[k]) == 2:
        a2.append(a1[k])
if len(a2)>=1:
    a2.sort()
    print("字串中最大質數為:"+a2[-1])
else:
    print("No prime found")  