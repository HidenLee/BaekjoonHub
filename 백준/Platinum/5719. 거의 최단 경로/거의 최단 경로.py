import sys
from collections import deque

def dijkstra(graph, costlist, s):
    minload = [[]for x in range(n)]
    queue = deque([(s, 0)])
    costlist[s] = 0
    while queue:
        # print("queue", queue)
        node, cost = queue.popleft()
        if cost > costlist[node]:
            continue
        for nnode, ncost in graph[node]:
            if ncost != -1:
                if costlist[nnode] > costlist[node] + ncost:
                    costlist[nnode] = costlist[node]+ncost
                    minload[nnode].clear()
                    minload[nnode].append(node)
                    queue.append((nnode, ncost))
                    # print("update", node, nnode, minload)
                elif costlist[nnode] == costlist[node] + ncost:
                    minload[nnode].append(node)
                    # print("add", node, nnode, minload)
    # print(minload)
    return minload

def bfs(d, minload, visit, graph):
    queue = deque([d])
    visit[d] = True
    while queue:
        node = queue.popleft()
        for nnode in minload[node]: # node: 도착, nnode: 출발
            if visit[nnode]==False:
                queue.append(nnode)
                visit[nnode]=True
            for index in range(len(graph[nnode])):
                if graph[nnode][index][0] == node:
                    graph[nnode][index][1] = -1
    return graph

while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        exit()
    graph = [[]for x in range(n)]
    s, d = map(int, sys.stdin.readline().split())
    for i in range(m):
        u, v, p = map(int, sys.stdin.readline().split())
        graph[u].append([v, p])
    costlist = [1e10 for x in range(n)]

    # 최단 경로 구하기
    minload = dijkstra(graph, costlist, s)
    # 최단 경로 제거
    visit = [False for x in range(n)]
    bfs(d, minload, visit, graph)
    # 거의 최단 경로 구하기
    costlist = [1e10 for x in range(n)]
    dijkstra(graph, costlist, s)
    if costlist[d] == 1e10:
        print(-1)
    else:
        print(costlist[d])