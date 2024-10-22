# def findByDFS(start, end, visiited=set()):
#     if start == end:
#         return True
#     if table[start][end] or table[end][start]:
#         return True
#     visiited.add(start)

#     for idx, flag in enumerate(table[start]):
#         if flag and not idx in visiited and findByDFS(idx,end,visiited):
#             for visit in visiited:
#                 table[visit][end] = 1
#             table[start][end] = 1
#             return True
#     return False

def find(node):
    now = node
    brothers = set()
    while parents[now] != now:
        brothers.add(now)
        now = parents[now]
    for bro in brothers:
        parents[bro] = now
    return now



N = int(input())
M = int(input())
# table = [list(map(int,input().split())) for _ in range(N)]
parents = [x for x in range(N)]
for idx in range(N):
    for jdx, flag in enumerate(list(map(int,input().split()))):
        if flag:
            ip = find(idx)
            jp = find(jdx)
            parents[max(ip,jp)] = min(ip,jp)
target =  list(map(int,input().split()))
# print("YES" if all([findByDFS(target[i]-1,target[i+1]-1) for i in range(M-1)]) or N == 1 else "NO")
print("YES" if all([parents[target[i]-1]==parents[target[i+1]-1] for i in range(M-1)]) or N == 1 else "NO")
