N = int(input())
ans = 101
table = [[-1] * 19 for _ in range(19)]

def pprint(arr):
    print("!@#@!##")
    for _ in range(len(arr)):
        print(arr[_])
def func1(a):
    return int(a)-1

delta = [[0,1],[1,0],[1,1],[-1,1]]
def solve(x,y,c):
    table[y][x] = c
    for dt in delta:
        cnt = 1
        lflag = False
        rflag = False
        for i in range(1,20):
            lx, ly = x - dt[0]*i, y - dt[1]*i
            rx, ry = x + dt[0]*i, y + dt[1]*i
            if 0 <= lx < 19 and 0 <= ly < 19 and table[ly][lx] == c:
                cnt += 1
            else:
                lflag = True
            if 0 <= rx < 19 and 0 <= ry < 19 and table[ry][rx] == c:
                cnt += 1
            else:
                rflag = True
            if lflag and rflag or cnt > 5:
                break
        if cnt == 5:
            # pprint(table)
            return True
    
    return False

for i in range(1,N+1):
    x , y  = map(func1,input().split())
    if solve(x,y,i%2):
        ans = min(ans,i)
# pprint(table)
print(ans if ans != 101 else -1)