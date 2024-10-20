from collections import deque
N = int(input())
ipt = [list(map(int,input().split())) for _ in range(N)]
ans = [0]*(N+1)
ans[0] = 1
# deq = deque[(1,0)]
# while deq:
#     now_node,now_depth = deq.pop()
#     if ans[now_node]:
#         continue
#     if len(ipt[now_node-1]) == 2:
#         ans[now_node] = ipt[now_node-1][0]


def costof(N):
    if ans[N]:
        return ans[N]
    if len(ipt[N-1]) == 2:
        ans[N] = ipt[N-1][0]
        return ans[N]
    


    ans[N] = ipt[N-1][0] + max([costof(nxt) if nxt != -1 else 0 for nxt in ipt[N-1][1:]])
    return ans[N]

for i in range(1, N + 1):
    costof(i)

for i in range(1, N + 1):
    print(ans[i])
