import heapq
MAX_DISTANCE = 10 ** 9 

N,M = map(int,input().split())
# arr = [[0]*(N+1) for _ in range(N+1)]
# for a,b,d in [tuple(map(int,input().split())) for _ in range(M)]:
#     arr[a][b] = d
#     arr[b][a] = d

arr = [[] for _ in range(N+1)]
for a,b,d in [tuple(map(int,input().split())) for _ in range(M)]:
    arr[a].append((b,d))
    arr[b].append((a,d))

def fox(start):
    dist = [MAX_DISTANCE]*(N+1)
    dist[start] = 0
    pq = [(0,start)]

    while pq:
        now_dist, now_node = heapq.heappop(pq)
        if now_dist > dist[now_node]:
            continue
        # for nxt_node, nxt_curl in enumerate(arr[now_node]):
        for nxt_node, nxt_curl in arr[now_node]:
            if nxt_curl == 0:
                continue
            nxt_curl *= 2
            if dist[nxt_node] > nxt_curl + now_dist:
                dist[nxt_node] = nxt_curl + now_dist
                heapq.heappush(pq,(dist[nxt_node],nxt_node))
    return dist

def wolf(start):
    dist = [[MAX_DISTANCE,MAX_DISTANCE] for _ in range(N+1)]
    dist[start][1] = 0
    pq = [(0,start,1)]

    while pq:
        now_dist, now_node, now_fast = heapq.heappop(pq)
        if now_dist > dist[now_node][now_fast]:
            continue

        for nxt_node, nxt_curl in arr[now_node]:
        # for nxt_node, nxt_curl in enumerate(arr[now_node]):
            if nxt_curl == 0:
                continue
            if not now_fast:
                nxt_curl *= 4
            nxt_fast = 1 - now_fast
            if dist[nxt_node][nxt_fast] > nxt_curl + now_dist:
                dist[nxt_node][nxt_fast] = nxt_curl + now_dist
                heapq.heappush(pq,(dist[nxt_node][nxt_fast],nxt_node,nxt_fast))
    return dist


fox_dist = fox(1)
wolf_dist = wolf(1)
print(sum([1 if fox_dist[i] < min(wolf_dist[i]) else 0 for i in range(2,N+1)]))
