from collections import deque
N, M = map(int,input().split())
route = {}
for _ in range(N+M):
    fr, to = map(int,input().split())
    route[fr] = to
dist = [100000]*101
deq = deque([(1,0)])
while deq:
    now, depth = deq.popleft()
    dist[now] = min(dist[now],depth)
    # if now == 100:
    #     print(depth)
    #     break
    if now in route:
        deq.append((route[now],depth))
        continue
    for nxt in [x for x in range(now+1,now+7) if x <101]:
        if dist[nxt] > depth + 1:
            dist[nxt] = depth + 1
            deq.append((nxt,depth+1)) 
print(dist[100])