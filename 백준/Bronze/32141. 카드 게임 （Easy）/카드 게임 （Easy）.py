N, M = map(int,input().split())
for idx, atk in enumerate(map(int,input().split())):
    M -= atk
    if M <=0:
        print(idx+1)
        break
else:
    print(-1)