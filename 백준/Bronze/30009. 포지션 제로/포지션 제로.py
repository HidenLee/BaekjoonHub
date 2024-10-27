
N = int(input())
X,Y,R = map(int,input().split())
cnt = [0,0]
for _ in range(N):
    ipt = int(input())
    if ipt in [X-R,X+R]:
        cnt[1] += 1
        continue
    if ipt in range(X-R,X+R):
        cnt[0] += 1
        continue
print(*cnt)