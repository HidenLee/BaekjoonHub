def solution(x, y, n):
    from collections import deque
    visit = [10e7]* 1000001
    dq = deque([x])
    visit[x] = 0
    while dq:
        now = dq.pop()
        if now == y:
            return visit[now]
        for nxt in [now*2,now*3,now+n]:
            if nxt <= y and visit[nxt] > visit[now] + 1:
                dq.appendleft(nxt)
                visit[nxt] = visit[now] + 1
    
    
    
    return -1