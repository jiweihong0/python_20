count=int(input("組數為:"))
counts=[]
for i in range(count):
    counts.append(input("第%d組"%(i+1)).split(" "))
for j in range(count):
    print("第%d組應收費用:%d"%(j+1,int(counts[j][0])*250+int(counts[j][1])*175))
