from collections import deque
import heapq
def solution(N, road, K):
    MAXIMUM_COST_VALUE = K*10000
    graph = {x:{y:MAXIMUM_COST_VALUE for y in range(1,N+1)} for x in range(1,N+1)}
    
    for node1, node2, cost in road:
        graph[node1][node2] = min(graph[node1][node2],cost)
        graph[node2][node1] = min(graph[node2][node1],cost)
    
    dist = [MAXIMUM_COST_VALUE for _ in range(N+1)]
    dist[1] = 0
    
    dq = deque([(1,K)])
    while dq:
        now, remain = dq.popleft()
        for nxt in range(1,N+1):
            if graph[now][nxt] == MAXIMUM_COST_VALUE:
                continue
            if dist[nxt] >= graph[now][nxt] + dist[now] :
                dist[nxt] = graph[now][nxt] + dist[now]
                if remain >= graph[now][nxt]:
                    dq.append((nxt,remain-graph[now][nxt]))
    return sum([1 if x <=K else 0 for x in dist])
