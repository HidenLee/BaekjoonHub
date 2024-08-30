N, M = map(int,input().split())
route = dict()
for _ in range(M):
    u, v = map(int,input().split())
    if u in route: 
        route[u].append(v)
    else:
        route[u] = [v]
S = int(input())
fans = list(map(int,input().split()))
# print(route)

from collections import deque
def bfs(node):
    visit = set()
    deq = deque([node])
    while deq:
        now = deq.pop()
        if now in fans:
            # print("fan",now)
            continue
        if not now in route:
            # print("end",now)
            return False
        visit.add(now)
        for nxt in route[now]:
            if not nxt in visit:
                deq.appendleft(nxt)
    return True
if bfs(1):
    print("Yes")
else:
    print("yes")
