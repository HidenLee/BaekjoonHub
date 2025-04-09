import sys
input = sys.stdin.readline

def left():
    global table
    for idx in range(len(table)):
        top = 0
        for jdx in range(1,len(table)):
            if table[idx][jdx] != 0:
                temp = table[idx][jdx]
                table[idx][jdx] = 0
                if table[idx][top] == 0:
                    table[idx][top] = temp
                elif table[idx][top] == temp:
                    table[idx][top] *= 2
                    top += 1
                else:
                    top += 1
                    table[idx][top] = temp
def up():
    global table
    for idx in range(len(table)):
        top = 0
        for jdx in range(1,len(table)):
            if table[jdx][idx] != 0:
                temp = table[jdx][idx]
                table[jdx][idx] = 0
                if table[top][idx] == 0:
                    table[top][idx] = temp
                elif table[top][idx] == temp:
                    table[top][idx] *= 2
                    top += 1
                else:
                    top += 1
                    table[top][idx] = temp

def down():
    global table
    for idx in range(len(table)):
        top = len(table) - 1
        for jdx in range(len(table)-2,-1,-1):
            if table[jdx][idx] != 0:
                temp = table[jdx][idx]
                table[jdx][idx] = 0
                if table[top][idx] == 0:
                    table[top][idx] = temp
                elif table[top][idx] == temp:
                    table[top][idx] *= 2
                    top -= 1
                else:
                    top -= 1
                    table[top][idx] = temp

def right():
    global table
    for idx in range(len(table)):
        top = len(table) - 1
        for jdx in range(len(table)-2,-1,-1):
            if table[idx][jdx] != 0:
                temp = table[idx][jdx]
                table[idx][jdx] = 0
                if table[idx][top] == 0:
                    table[idx][top] = temp
                elif table[idx][top] == temp:
                    table[idx][top] *= 2
                    top -= 1
                else:
                    top -= 1
                    table[idx][top] = temp

delta = {"L": left, "U" : up, "D" : down, "R" : right}
MAX_DEPTH = 10
initial_max = 0
table = []
for _ in range(int(input())):
    ipt = list(map(int,input().split()))
    initial_max = max(initial_max,max(ipt))
    table.append(ipt)

stack = [("",True,table,initial_max)]
ans = initial_max
memo = [0]*(MAX_DEPTH+1)

def dfs(depth):
    global table, ans
    local_max = 0
    for _ in range(len(table)):
        local_max = max(local_max,max(table[_]))

    if local_max <= memo[depth] : return

    if depth == 10:
        ans = max(ans,local_max)
        if memo[10] < ans:
            temp = ans
            for i in range(10,0,-1):
                memo[i] = temp
                temp //= 2
        return
    
    origin = [[table[i][j] for j in range(len(table))] for i in range(len(table))]
    for keyw in delta.keys():
        delta[keyw]()
        if origin == table:
            continue
        dfs(depth+1)
        table = [[origin[i][j] for j in range(len(origin))] for i in range(len(origin))]
        

dfs(0)
print(ans)