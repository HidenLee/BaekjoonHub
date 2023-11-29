#sw아카데미 1767 프로세서 연결하기

dx=[0,0,1,-1]
dy=[1,-1,0,0]

def dfs(depth,cnt,connect):
    global answer
    global max_connect
    if depth==l_c:
        if connect>max_connect:
            max_connect=connect
            answer=cnt
        elif connect==max_connect and answer>cnt:
            answer=cnt
        return
    #이렇게 반복문 형태로 돌려주면서 시간초과 줄여줬습니다.
    for k in range(depth,l_c):
        cx,cy=core[k]
        for d in range(4):
            nx=cx
            ny=cy
            flag=False
            tmp=set()
            leng=0
            #상하좌우 살피면서 연결여부를 판단
            while True:
                nx+=dx[d]
                ny+=dy[d]
                #범위벗어난다->연결이 되면 가능하다 표시하고 나가기
                if nx<0 or nx>=N or ny<0 or ny>=N:
                    flag=True
                    break
                #코어를 만나면 못함
                if room[nx][ny]==1:
                    break
                #다른 전선을 만나면 못함
                tmp.add((nx,ny))
                leng+=1
            #가능하다면 전선을 연결
            if flag:
                for px,py in tmp:
                    room[px][py]=1
                #현재 연결한 코어 다음 코어로 넘어간다.
                dfs(k+1,cnt+leng,connect+1)

                for px,py in tmp:
                    room[px][py]=0


T=int(input())

for t in range(T):
    answer=1e9
    max_connect=0
    N=int(input())
    room=[]
    core=[]
    for i in range(N):
        tmp=list(map(int,input().split()))
        for j in range(1,N-1):
            if i==0 or i==N-1:
                break
            if tmp[j]==1:
                core.append([i,j])
        room.append(tmp)
    l_c=len(core)
    visited=[[False]*N for _ in range(N)]

    dfs(0,0,0)

    print("#%d %d"%(t+1,answer))