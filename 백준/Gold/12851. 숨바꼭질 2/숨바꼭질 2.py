N, K = map(int,input().split())
from collections import deque

deq = deque([N])
MAX_VALUE = 10**6 +1
visit = [0] * MAX_VALUE
dist = [MAX_VALUE] * MAX_VALUE
dist[N] = 0
visit[N] = 1
flag = MAX_VALUE
while deq:
    now = deq.popleft()
    if dist[now] > flag:
        continue
    if now == K:
        flag = dist[now]

    for nxt in [now-1,now+1,now*2]:
        if 0<= nxt < MAX_VALUE and dist[nxt] >= dist[now]+1:
            dist[nxt] = dist[now]+1
            visit[nxt] += 1
            deq.append(nxt)
print(dist[K])
print(visit[K])