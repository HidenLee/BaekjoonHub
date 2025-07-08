def solution(k, dungeons):
    answer = 0
    N = len(dungeons)
    for i in range(N):
        visited = [False]*N
        visited[i] = True
        if k < dungeons[i][0]:
            continue
        stack = [(1,1,k-dungeons[i][1],visited)]
        while stack:
            depth, count, remain, memory = stack.pop()
            if (N-depth) + count <= answer:
                continue
            answer = max(count,answer)
            for j in range(N):
                if not memory[j] and remain >= dungeons[j][0]:
                    memory[j] = True
                    stack.append((depth+1,count+1,remain-dungeons[j][1],[x for x in memory]))
                    memory[j] = False
                
                
    return answer