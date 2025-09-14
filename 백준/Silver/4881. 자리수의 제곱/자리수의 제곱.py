def trans(x):
    return sum([int(i)**2 for i in str(x)])

def cycle(x):
    visit = {}
    nxt = x
    depth = 1
    while nxt not in visit:
        visit[nxt] = depth
        nxt = trans(nxt)
        depth += 1
    return visit     

while True:
    x,y = map(int,input().split())
    if x == 0 and y == 0:
        break
    cx = cycle(x)
    cy = cycle(y)
    answer = min([(cx[i] + cy[i]) for i in cx if i in cy] +[float('inf')])
    print(x,y,answer if answer != float('inf') else 0)