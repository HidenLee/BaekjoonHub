
import heapq
maxV = 200000 * 1000 + 1
def dijkstra(start,destination):
    if start == destination:
        return 0
    dist = [maxV for _ in range(N+1)]   
    dist[start] = 0

    pq = []
    heapq.heappush(pq,(0,start))
    while pq:
        now_dist, now_node = heapq.heappop(pq)
        if now_dist > dist[now_node]:
            continue

        for nxt_node, nxt_dist in graph[now_node]:
            if dist[nxt_node] > now_dist + nxt_dist:
                dist[nxt_node] = now_dist + nxt_dist
                heapq.heappush(pq,(dist[nxt_node],nxt_node))
    return dist[destination]


N, E = map(int,input().split())
graph = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
v1, v2 = map(int,input().split())

ans = min(dijkstra(1,v1)+dijkstra(v1,v2)+dijkstra(v2,N),dijkstra(1,v2)+dijkstra(v2,v1)+dijkstra(v1,N))
print(ans if ans < maxV else -1)