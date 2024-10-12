N, M =map(int,input().split())

house = []
chick = []
maximumV = 10 ** 9
for idx in range(N):
    ipt = list(map(int,input().split()))
    for jdx,elm in enumerate(ipt):
        if elm == 1:
            house.append((idx,jdx))
        elif elm == 2:
            chick.append((idx,jdx))

ans = maximumV
from itertools import combinations

for choices in combinations(chick,M):
    chickDist = 0
    for hx, hy in house:
        chickDist += min([abs(hx-cx)+abs(hy-cy) for cx, cy in choices])
    ans = min(chickDist,ans)
print(ans)
