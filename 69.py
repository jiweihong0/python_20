a=input()
a1=[]
a2=[]
a3=''
for i in range(len(a)//5):
    a1.append(a[i*5:(i*5)+5])
for j in range(len(a1)):
    if a1[j]=="-----":
        a2.append(0)
    if a1[j]==".----":
        a2.append(1)
    if a1[j]=="..---":
        a2.append(2)
    if a1[j]=="...--":
        a2.append(3)
    if a1[j]=="....-":
        a2.append(4)
    if a1[j]==".....":
        a2.append(5)
    if a1[j]=="-....":
        a2.append(6)
    if a1[j]=="--...":
        a2.append(7)
    if a1[j]=="---..":
        a2.append(8)
    if a1[j]=="----.":
        a2.append(9)
for k in a2:
    a3+=str(k)
print(a3)