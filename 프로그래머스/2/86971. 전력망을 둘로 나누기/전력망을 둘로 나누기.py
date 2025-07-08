def solution(n, wires):
    answer = n
    
    route = {x:{} for x in range(1,n+1)}
    for wire in wires:
        route[wire[0]][wire[1]] = True
        route[wire[1]][wire[0]] = True
    for wire in wires:
        route[wire[0]][wire[1]] = False
        route[wire[1]][wire[0]] = False
        visited = [False for _ in range(n+1)]
        compare = []
        for i in range(1,n+1):
            if visited[i]:
                continue
            visited[i] = True
            stack = [i]
            count = 0
            while stack:
                now = stack.pop()
                count += 1
                for nxt in route[now].keys():
                    if route[now][nxt] and not visited[nxt]:
                        visited[nxt] = True
                        stack.append(nxt)
            compare.append(count)
        answer = min(answer,abs(compare[0]-compare[1]))
        route[wire[0]][wire[1]] = True
        route[wire[1]][wire[0]] = True
    
    
    return answer