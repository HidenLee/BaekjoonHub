N, M, H = map(int,input().split())
dic = {tuple(map(lambda x: int(x)-1,input().split())):True for _ in range(M)}
def game():
    for i in range(N):
        now = i
        depth = 0
        while depth < H:
            if (depth,now) in dic:
                now += 1
            elif (depth,now-1) in dic:
                now -= 1
            depth += 1
        if now != i:
            return False
    return True
ans = 4
def func(cnt,nowI,nowJ):
    global ans
    if game():
        ans = min(cnt,ans)
        return 
    if cnt == 3 or cnt >= ans:
        return 


    for idx in range(nowI,H):
        for jdx in range(nowJ if idx == nowI else 0,N-1):
            if (idx,jdx) not in dic and (idx,jdx+1) not in dic and (jdx == 0 or (idx,jdx-1) not in dic):
                dic[(idx,jdx)] = True
                func(cnt+1,idx,jdx+2)
                del dic[(idx,jdx)]
func(0,0,0)
print(ans if ans != 4 else -1)

