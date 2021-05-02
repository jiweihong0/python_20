aaaa = int(input("輸入度數:"))
aa = aaa = 0
if aaaa<=120:
    aa=aaaa*2.10
    aaa=aaaa*2.10
elif aaaa>120 and aaaa<=330:
    aa=120*2.10+(aaaa-120)*3.02
    aaa=120*2.10+(aaaa-120)*2.68
elif aaaa>330 and aaaa<=500:
    aa=120*2.10+210*3.02+(aaaa-330)*4.39
    aaa=120*2.10+210*2.68+(aaaa-330)*3.61
elif aaaa>500 and aaaa<=700:
    aa=120*2.10+210*3.02+170*4.39+(aaaa-500)*4.97
    aaa=120*2.10+210*2.68+170*3.61+(aaaa-500)*4.01
elif aaaa>700:
    aa=120*2.10+210*3.02+170*4.39+200*4.97+(aaaa-700)*5.63
    aaa=120*2.10+210*2.68+170*3.61+200*4.01+(aaaa-700)*4.50
print("Summer months:"+str(aa)+"\n"+"Non-Summer months:"+str(aaa))