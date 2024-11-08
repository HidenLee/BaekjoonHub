R, C = map(int,input().split())
table = [list(input()) for _ in range(R)]
visited = [[False]*C for _ in range(R)]
from collections import deque
ans = [0,0]
delta = [(0,1),(1,0),(0,-1),(-1,0)]
for idx in range(R):
    for jdx in range(C):
        if table[idx][jdx] == "#" or visited[idx][jdx] == True:
            continue
        deq = deque([(idx,jdx)])
        v = 0
        k = 0
        node_set = set([(idx,jdx)])
        while deq:
            oy,ox = deq.pop()

            for ny, nx in [(oy+dy,ox+dx) for dy,dx in delta if 0<=oy+dy<R and 0<=ox+dx<C]:
                if table[ny][nx] != "#" and not visited[ny][nx] and not (ny,nx) in node_set:
                    deq.appendleft((ny,nx))
                    node_set.add((ny,nx))



        for node in list(node_set):
            if table[node[0]][node[1]] == "k":
                k += 1
            elif table[node[0]][node[1]] == "v":
                v += 1
            visited[node[0]][node[1]] = True
        # print(idx,jdx,k,v)
        ans[0] += k if k > v else 0 
        ans[1] += v if v >= k else 0

print(*ans)