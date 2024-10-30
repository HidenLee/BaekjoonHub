cnt = 0
for idx, ipt in enumerate(map(int,input().split())):
    if ipt > ((idx+2)//2)*100:
        print("hacker")
        exit()
    cnt += ipt
print("draw" if cnt >= 100 else "none")