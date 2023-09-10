from collections import deque
from copy import deepcopy


def pprint(lst):
    for slst in lst:
        print(slst)
    print()



def gravity(table,d):
    # -1:fail, 0:keep, 1:success
    table, Bflag = move(table, d,'B')
    if Bflag:
        return table, -1
    else:
        table, Rflag = move(table, d,'R')
        table, Bflag = move(table, d,'B')
        if Bflag:
            return table, -1
        elif Rflag:
            return table, 1
        else:
            return table, 0


def move(table, diridx, color):
    global O
    if color == 'R':
        x, y = table[-2][0], table[-2][1]
    else: # B
        x, y = table[-1][0], table[-1][1]

    dirdict = [(1,0),(0,1),(-1,0),(0,-1)]
    
    table[y][x] = '.'

    nx, ny = x , y 
    while table[ny + dirdict[diridx][1]][nx + dirdict[diridx][0]] in ['.','O'] :
        nx += dirdict[diridx][0]
        ny += dirdict[diridx][1]
        if nx == O[0] and ny == O[1]:
            if color == 'R':
                table[-2][0], table[-2][1] = nx, ny
            else: # B
                table[-1][0], table[-1][1] = nx, ny
            return table, True
    table[ny][nx] = color

    if color == 'R':
        table[-2][0], table[-2][1] = nx, ny
    else: # B
        table[-1][0], table[-1][1] = nx, ny

    return table, False




N, M = map(int,input().split())
table = [list(input()) for _ in range(N)]
for y in range(1,N-1):
    for x in range(1,M-1):
        if table[y][x] == 'R':
            R = [x,y]
        elif table[y][x] == 'B':
            B = [x,y]
        elif table[y][x] == 'O':
            O = [x,y]
table.append(R)
table.append(B)



isvisited = set([])
dq = deque([(table,0,'0'),(table,1,'1'),(table,2,'2'),(table,3,'3')])
ispass = False
while dq:
    maze, diridx, route = dq.popleft()
    isvisited.add(route)
    if len(route) > 10:
        continue
    nxt = deepcopy(maze)
    nxt, status = gravity(nxt,diridx)
    # print("route: ",route)
    # pprint(nxt)
    if status == 1:
        ispass = True
        print(len(route))
        # print('congraturation!!!!!!',route)
        break
    elif status == -1:
        pass
        # print('faillll',route)
    else:
        for d in range(4):
            if d != diridx and route+str(d) not in isvisited:
                dq.append((nxt,d,route+str(d)))

if not ispass:
    print(-1)

