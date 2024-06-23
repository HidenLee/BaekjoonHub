# https://www.acmicpc.net/problem/1325
N, M = map(int,input().split())
trust = [[] for _ in range(N+1)]
maxSize = -1
for _ in range(M):
    A, B = map(int,input().split())
    trust[B].append(A)

# fail - time out
def sol_dfs(node):
    stack = [node]
    visit = [False]*(N+1)
    visit[node] = True
    cnt = 0
    while stack:
        old = stack.pop()
        if visit[old]:
            continue
        visit[old] = True
        cnt += 1
        for new in trust[old]:
            if not visit[new]:
                stack.append(new)
    return visit.count(True)


# fail
from collections import deque
def sol_bfs(node):
    dq = deque([node])
    visit = [False] *(N+1)
    visit[node] = True
    cnt = 0
    while dq:
        old = dq.popleft()
        cnt += 1
        for nxt in trust[old]:
            if visit[nxt]:
                continue
            else:
                dq.append(nxt)
                visit[nxt] = True
    return sum(visit)

def sol_Bffs(node):
    q = deque()
    q.append(node)
    infected = [False] * (N + 1)
    infected[node] = True
    while q:
        node = q.popleft()
        for nextNode in trust[node]:
            if infected[nextNode] == True:
                continue
            else:
                q.append(nextNode)
                infected[nextNode] = True

    return infected.count(True)

for i in range(1,N+1):
    temp = sol_Bffs(i)
    if maxSize < temp:
        maxSize = temp
        ans = [i]
    elif maxSize == temp:
        ans.append(i)

print(*ans)
