
while True:
    n=input("檢測的字串(end結束)：")
    if n == "end":
        break
    m=input("檢測的單一字元：")
    print("字元%s出現的次數為：%d" %(m,n.count(m)))

print("檢測結束")