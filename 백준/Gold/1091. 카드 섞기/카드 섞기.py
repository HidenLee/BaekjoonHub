N = int(input())
P = list(map(int,input().split()))
shuffledict = {idx:X for idx, X in enumerate(list(map(int,input().split())))}
arr = [i % 3 for i in range(N)]
def isSame():
    for i in range(N):
        if arr[i] != i % 3:
            return False
    return True

def shuffle():
    global arr
    arr = [arr[shuffledict[i]]  for i in range(N)]

def isDone():
    for i in range(N):
        if arr[i] % 3 != P[i]:
            return False
    return True
flag = False
if not isDone():
    shuffle()
    cnt = 1
    while not isDone():
        # print("cnt: ",cnt," arr: ",arr)
        shuffle()
        cnt += 1
        if isSame():
            print(-1)
            flag = True
            break
    if not flag:
        print(cnt)
else:
    print(0)