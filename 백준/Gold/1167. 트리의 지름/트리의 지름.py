dic = { line[0]:[(line[k],int(line[k+1])) for k in range(len(line)-1) if k%2 and line[k] != -1] for line in [tuple(map(int,input().split())) for _ in range(int(input()))] }
from collections import deque
def find_farest_from(n):
    visit = [False]*(len(dic)+1)
    visit[n] = True
    deq = deque([(n,0)])
    returns = [0,0]
    while deq:
        now, dist = deq.pop()
        flag = False
        for nxt, cost in dic[now]:
            if visit[nxt]:
                continue
            else:
                flag = True
                deq.appendleft((nxt,dist+cost))
                visit[nxt] = True
        if not flag:
            if returns[1] < dist:
                returns = [now,dist]
    return returns
# diameter of a tree can get by these flow
# get farest node (let me call it f node) from a random pick node
# then get the shortest way cost between f node and farest node from f node 
print(find_farest_from(find_farest_from(1)[0])[1])
