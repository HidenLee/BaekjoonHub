N, K = map(int,input().split())
from collections import deque

deq = deque([N])
MAX_VALUE = 10**6 +1
dist = [MAX_VALUE] * MAX_VALUE
dist[N] = 0
while deq:
    now = deq.popleft()
    if now == K:
        print(dist[now])
        break

    for idx, nxt in enumerate([now-1,now+1,now*2]):
        if 0<= nxt < MAX_VALUE:
            temp = dist[now]
            if idx !=2:
                temp += 1
            if dist[nxt] >= temp:
                dist[nxt] = temp
                deq.append(nxt)
