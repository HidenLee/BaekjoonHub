N, M = map(int,input().split())
dic = {x:x for x in range(0,N+1)}
# common parent : child
def find(node):
    stack = [dic[node]]
    while stack:
        now = stack.pop()
        if dic[now] == now:
            dic[node] = now
            break
        stack.append(dic[now])

    # if dic[node] == node:
    #     return node
    # dic[node] = find(dic[node])
    return dic[node]

def union(node1, node2):
    node1_parent = find(node1)
    node2_parent = find(node2)
    dic[max(node1_parent,node2_parent)] = min(node1_parent,node2_parent)

def calc(node1,node2):
    return find(node1) == find(node2)

for i,a,b in [tuple(map(int, input().split())) for _ in range(M)]:
    
    if i == 0:
        union(a,b)
    else:
        print("YES" if calc(a,b) else "NO")
