121
1231
12421
0
while(True):
    ipt = input()
    if ipt == "0":
        break
    print("yes" if ipt[:len(ipt)//2] == ipt[len(ipt)-(len(ipt)//2):][::-1] else "no")
