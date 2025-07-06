def solution(n, results):
    
    route = {x:set() for x in range(1,n+1)}
    count = [0 for _ in range(n+1)]
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
    print(count)
    print(route)
    answer = 0
    for k in range(1,n+1):
        if count[k] == n-1:
            answer += 1
    return answer

# print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]), 2)
# print(solution(7, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [5,6], [6,7]]), 4)
# print(solution(6, [[1,2], [2,3], [3,4], [4,5], [5,6]]), 6)
# print(solution(5, [[1, 4], [4, 2], [2, 5], [5, 3]]), 5)
# print(solution(5, [[3, 5], [4, 2], [4, 5], [5, 1], [5, 2]]), 1)
# print(solution(3, [[1,2],[1,3]]), 1)
# print(solution(6, [[1,6],[2,6],[3,6],[4,6]]), 0)
# print(solution(8, [[1,2],[3,4],[5,6],[7,8]]),0)
# print(solution(9, [[1,2],[1,3],[1,4],[1,5],[6,1],[7,1],[8,1],[9,1]]), 1)
# print(solution(6, [[1,2],[2,3],[3,4],[4,5],[5,6],[2,4],[2,6]]), 6)
# print(solution(4, [[4,3],[4,2],[3,2],[3,1],[4,1], [2,1]]), 4)
# print(solution(3,[[3,2],[3,1]]), 1)
# print(solution(4, [[1,2],[1,3],[3,4]]), 1)