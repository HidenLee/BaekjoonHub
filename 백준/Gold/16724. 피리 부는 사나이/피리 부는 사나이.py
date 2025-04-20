N, M = map(int, input().split())

parent = [i for i in range(N*M)]

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]] 
        x = parent[x]
    return x

def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        parent[y] = x

dic = {"D":(1,0), "U":(-1,0), "R":(0,1), "L":(0,-1)}

table = [list(input()) for _ in range(N)]
for y in range(N):
    for x in range(M):
        ny, nx = y + dic[table[y][x]][0], x + dic[table[y][x]][1]
        if 0 <= ny < N and 0 <= nx < M:
            union(y*M+x, ny*M+nx)
roots = set()
for i in range(N * M):
    roots.add(find(i))
print(len(roots))