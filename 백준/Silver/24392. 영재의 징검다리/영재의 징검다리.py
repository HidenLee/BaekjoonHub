N, M = map(int,input().split())
pre = list(map(int,input().split()))
for _ in range(1,N):
    nxt = list(map(int,input().split()))
    for jdx in range(M):
        if nxt[jdx] == 1:
            nxt[jdx] = sum([pre[x] for x in [jdx-1,jdx,jdx+1] if 0<=x<M]) % 1000000007
    pre = nxt
if N == 1 :
    nxt = pre 
print(sum(nxt)%1000000007)
