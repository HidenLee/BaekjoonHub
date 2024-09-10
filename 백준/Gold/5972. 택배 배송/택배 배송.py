N,  M = map(int,input().split())
MAXIMUM = 50000*1000+1
dist = [MAXIMUM]*(N+1)
route = {x:[] for x in range(1,N+1)}
for _ in range(M):
    a,b,c = map(int,input().split())
    route[a].append((b,c))
    route[b].append((a,c))

dist[1] = 0
import heapq
queue = []
heapq.heappush(queue,(dist[1],1))
while(queue):
    now_dist, now_node = heapq.heappop(queue)
    if dist[now_node] < now_dist:
        continue
    for nxt_node, nxt_dist in route[now_node]:
        temp = nxt_dist + now_dist
        if dist[nxt_node] > temp:
            dist[nxt_node] = temp
            heapq.heappush(queue,(temp,nxt_node))
print(dist[N])