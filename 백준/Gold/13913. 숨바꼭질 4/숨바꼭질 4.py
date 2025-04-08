N, K = map(int,input().split())
from collections import deque

deq = deque([N])
MAX_VALUE = 10**6
linkedRef = [MAX_VALUE+1] * (MAX_VALUE+1)
linkedRef[N] = -1
while deq:
    now = deq.popleft()
    if now == K:
        ans = deque([now])
        k = linkedRef[now]
        while k != -1:
            ans.appendleft(k)
            k = linkedRef[k]
        print(len(ans)-1)
        print(*ans)
        break
    for nxt in [now-1,now+1,now*2]:
        if 0<= nxt <= 10**6 and linkedRef[nxt] == MAX_VALUE+1:
            linkedRef[nxt] = now
            deq.append(nxt)