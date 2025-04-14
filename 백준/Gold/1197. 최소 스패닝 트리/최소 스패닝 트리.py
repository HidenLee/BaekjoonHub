import heapq
def find(n):
    if parent[n] != n:
        parent[n] = find(parent[n])
    return parent[n]

def union(n,m):
    n = find(n)
    m = find(m)
    if n > m :
        parent[m] = n
    else:
        parent[n] = m

V, E = map(int,input().split())
# table = [tuple(map,int(input().split())) for _ in range(E)]
table = []
for _ in range(E):
    a, b, c = map(int,input().split())
    heapq.heappush(table,((c,a,b))) 
parent = list(range(V+1))
ans = 0
cnt = 0
while table and cnt < V-1:
    c,a,b = heapq.heappop(table)
    if find(a) != find(b):
        ans += c
        union(a,b)

print(ans)