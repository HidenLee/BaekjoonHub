def solution(n, results):
    
    route = {x:set() for x in range(1,n+1)}
    count = [0 for _ in range(n+1)]
    answer = 0
    for fr,to in results:
        route[fr].add(to)
    for i in range(1,n+1):
        visit = [False]*(n+1)
        stack = [i]
        while stack:
            now = stack.pop()
            for nxt in route[now]:
                if not visit[nxt]:
                    stack.append(nxt)
                    visit[nxt] = True
                    route[i].add(nxt)
                    count[nxt] += 1
        count[i] += len(route[i])
        
    for k in range(1,n+1):
        if count[k] == n-1:
            answer += 1
    return answer

