a=input("請輸入一串小寫英文:")
b=['a','e','i','o','u']
c=[]
e=''
for x in a: 
    if x in b:
        c.append(".")
    else:
        c.append(x)        
for d in c:
    e+=d
print(e)