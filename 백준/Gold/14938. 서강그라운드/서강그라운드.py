n, m, r = map(int,input().split())
items = list(map(int,input().split()))
dic = {x:[] for x in range(1,n+1)}
for x,y,z in [tuple(map(int,input().split())) for _ in range(r)]:
    dic[x].append((y,z))
    dic[y].append((x,z))

import heapq

MAX_CURL = 100 * 15 + 1
def getMaxValue(node):
    dist = [MAX_CURL] * (n+1)
    dist[node] = 0
    stack = [(0,node)]
    while stack:
        curl ,now = heapq.heappop(stack)

        if dist[now] < curl:
            continue

        for nxt, cost in dic[now]:
            if dist[nxt] > dist[now] + cost:
                dist[nxt] = dist[now] + cost
                heapq.heappush(stack,(dist[nxt],nxt))
    return sum([items[x-1] for x in range(n+1) if dist[x] <= m])
ans = 0
for i in range(1,n+1):
    ans = max(ans,getMaxValue(i))

print(ans)