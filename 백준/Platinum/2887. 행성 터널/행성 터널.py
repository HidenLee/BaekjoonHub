import sys
input = sys.stdin.readline

def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

def union(n,m):
    n = find(n)
    m = find(m)
    parent[m] = n

N = int(input())
table = [tuple(map(int,input().split())) for _ in range(N)]
ans = 0
line_cnt = 0
edges = []
for j in range(3):
    temp = sorted((table[i][j], i) for i in range(N))
    for i in range(1, N):
        edges.append((temp[i][0] - temp[i-1][0], temp[i-1][1], temp[i][1]))
edges.sort()
parent = list(range(N))
# for fr,to,cost in sorted([(ls[idx-1][1],ls[idx][1],ls[idx][0]-ls[idx-1][0]) for idx in range(1,N) for ls in [sorted([(table[i][j],i) for i in range(N)] ) for j in range(3)]], key=lambda X: X[2]):
for cost, fr, to in edges:
    if find(fr) != find(to):
        union(fr,to)
        ans += cost
        line_cnt += 1
        if line_cnt == N-1:
            break
print(ans)
