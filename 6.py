n=input("輸入質為:").split(",")
n.sort()
a=''
b=''
for i in n:
    a+=i
n.reverse()
for j in n:
    b+=j
print(int(b)-int(a))