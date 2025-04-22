import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
dic = {x:[] for x in range(1, N+1)}
for _ in range(N-1):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

visited = [False] * (N+1)
ans = 0

def dfs(now, prev):
    global ans
    visited[now] = True
    isINSSA  = False

    for nxt in dic[now]:
        if nxt != prev and not visited[nxt]:
            if not dfs(nxt, now):
                isINSSA = True

    if isINSSA:
        ans += 1
        return True
    return False
dfs(1,-1)
print(ans)