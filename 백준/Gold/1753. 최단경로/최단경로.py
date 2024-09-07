V, E = map(int,input().split())
K = int(input())
route = {}
for _ in range(E):
    s,e,v = map(int,input().split())
    if s in route:
        route[s].append((e,v))
    else:
        route[s] = [(e,v)]

dist = [10e9]*(V+1)
dist[K] = 0

# from collections import deque
# deq = deque([K])
# while deq:
#     now = deq.popleft()
#     if now in route:
#         for nxt, curl in route[now]:
#             if dist[nxt] > dist[now] + curl:
#                 dist[nxt] = dist[now] + curl
#                 deq.append(nxt)

import heapq
heap = []
heapq.heappush(heap,(0,K))
while heap:
    curl, now = heapq.heappop(heap)

    if dist[now] < curl:
        continue
    if not now in route:
        continue
    for nxt, cost in route[now]:
        if dist[nxt] > cost + curl:
            dist[nxt] = cost + curl
            heapq.heappush(heap,(dist[nxt],nxt))

for i in range(1,V+1):
    if dist[i] == 10e9:
        print("INF")
        continue
    print(dist[i])
