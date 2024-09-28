# https://www.acmicpc.net/problem/2638
def pprint(arr):
    print()
    for _ in range(len(arr)):
        print(arr[_])


N ,M = map(int,input().split())
# remain = 0
# def func1(arr):
#     global remain
#     remain += sum(arr)
#     return arr

# arr = [func1(list(map(int,input().split()))) for _ in range(N)]

delta = [(1,0),(0,1),(-1,0),(0,-1)]
arr = [["-1"]*M]
cheese = []
_ = input().split()
for idx in range(1,N-1):
    temp = list(input().split())
    for jdx,elm in enumerate(temp):
        if elm == "1":
            cheese.append((idx,jdx))
    temp[0] = "-1"
    temp[-1] = "-1" 
    arr.append(temp)
__ = input().split()
arr.append(["-1"]*M)

# 각 치즈에서 탐색으로 외벽까지 갈수있나 체크하자,
# 외벽에 도달했다면 그 치즈는 meltable, 경로가 외벽과 동일하다고 저장
# 외벽을 3이라고 적어둘까?
# 치즈를 매번 찾아야할까?
# 치즈 list가 필요할까?


def isAir(y,x):
    # print(y,x)
    global arr
    if not (0<=y<N and 0<=x<M):
        return 0
    if arr[y][x] == "-1":
        return 1
    if arr[y][x] == "1":
        return 0

    visit = [(y,x)]
    stack = [(y,x)]
    # print("stack: ",stack," y: ",y," x: ",x)
    while stack:
        # print(stack)
        oy ,ox = stack.pop()
        for ny, nx in [(dy+oy,dx+ox) for dy,dx in delta]:
            if 0 <= ny< N and 0 <= nx < M and not (ny,nx) in visit:
                if arr[ny][nx] == "-1":
                    for i, j in visit:
                        arr[i][j] = "-1"
                    arr[y][x] = "-1"
                    return 1
                elif arr[ny][nx] == "0":
                    visit.append((ny,nx))
                    stack.append((ny,nx))
    return 0

def ismeltable(oy,ox):
    return True if sum([isAir(dy+oy,dx+ox) for (dy,dx) in delta ]) >=2 else False

def melt():
    global arr
    global cheese
    day = 1
    while True:
        melting = []
        remain = []
        while cheese:
            # print(cheese)
            cy, cx = cheese.pop()
            if ismeltable(cy,cx):
                # print('hello')
                melting.append((cy,cx))
            else:
                remain.append((cy,cx))

        for i,j in melting:
            arr[i][j] = "0"
        if not remain:
            break

        cheese = remain
        day += 1
    return day
if cheese:
    print(melt())
else:
    print(0)    
# print("end")