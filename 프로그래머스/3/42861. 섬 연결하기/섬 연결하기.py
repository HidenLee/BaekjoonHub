def solution(n, costs):
    
    parents = [i for i in range(n)]
    
    def find(x):
        if parents[x] != x:
            parents[x] = find(parents[x])
        return parents[x]

    def union(x,y):
        px = find(x)
        py = find(y)
        if px != py:
            parents[py] = px
            return True
        return False

    answer = 0
    for fr, to, cost in sorted(costs,key=lambda X:X[2]):
        if union(fr,to):
            answer += cost
    return answer