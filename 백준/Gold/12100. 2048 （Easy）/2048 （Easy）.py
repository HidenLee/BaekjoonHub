def pprint(arr):
    for _ in range(len(arr)):
        print(arr[_])

def rotate90(arr):
    n = len(arr)
    return [[arr[j][n-i-1] for j in range(n)] for i in range(n)]

def rotate270(arr):
    n = len(arr)
    return [[arr[n-1-j][i] for j in range(n)] for i in range(n)]

def left(arr):
    n = len(arr)
    new_arr = [[0]*n for _ in range(n)]
    localMax = initial_max
    isChanged = False
    for idx in range(n):
        jdx = 0
        temp = -1
        for elm in arr[idx]:
            if temp == elm:
                elm *= 2
                jdx -= 1
                temp = -1
                isChanged = True
                localMax = max(localMax,elm)
            elif elm != 0:
                temp = elm
            if elm != 0:
                new_arr[idx][jdx] = elm
                jdx += 1
    return isChanged, new_arr, localMax

def right(arr):
    isChanged, arr, localMax = left(rotate90(rotate90(arr)))
    return isChanged, rotate270(rotate270(arr)), localMax

def up(arr):
    isChanged, arr, localMax = left(rotate90(arr))
    return isChanged, rotate270(arr), localMax

def down(arr):
    isChanged, arr, localMax = left(rotate270(arr))
    return isChanged, rotate90(arr), localMax

delta = {"L": left, "U" : up, "D" : down, "R" : right}
MAX_DEPTH = 5
initial_max = 0
table = []
for _ in range(int(input())):
    ipt = list(map(int,input().split()))
    initial_max = max(initial_max,max(ipt))
    table.append(ipt)

# pprint(left(table)[1])

stack = [("",True,table,initial_max)]

ans = initial_max

while stack:
    route, flag, arr, localMax = stack.pop()
    
    if len(route) == MAX_DEPTH:
        ans = max(ans, localMax)
        continue

    if localMax * 2**(MAX_DEPTH-len(route)) < ans:
        continue
    

    for nxt in [keyw for keyw in delta.keys() if flag or keyw != route[-1] ]:
        _ ,nxt_arr, nxt_localMax = delta[nxt](arr)
        stack.append((route+nxt,_,nxt_arr,nxt_localMax))

print(ans)