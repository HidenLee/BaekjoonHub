def totalbuildT2(b,builds):
    visited = []
    stack = builds[b][:]
    now = b
    while stack:
        # print(stack, times,visited)
        # now = stack.pop()
        if builds[now]: # 자식 노드 있음, 
            if all([1 if x in visited else 0 for x in builds[now]]): # 자식 탐색 끝
                times[now] += max([times[x] for x in builds[now]])
                visited.append(now)
                now = stack.pop()
                continue
            for nxt in builds[now]:
                if not nxt in visited: # 탐색하지 않은 자식으로 이동
                    stack.append(now)
                    now = nxt
                    break
        else: # 자식 노드 없음 -> 부모노드로 스택팝
            visited.append(now)
            now = stack.pop()
    return times[b]



T = int(input())
for test_case in range(T):
    N, K = map(int,input().split())
    builds = [[] for _ in range(N+1)]
    times  = list(map(int,input().split()))
    times = [0] + times
    for _ in range(K):
        a, b = map(int,input().split())
        builds[b].append(a)
    W = int(input())
    # rst = totalbuildT(W)
    rst = totalbuildT2(W,builds)
    print(rst)
