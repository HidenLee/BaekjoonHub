# https://www.acmicpc.net/problem/2961

N = int(input())
S = [0]*N
B = [0]*N
used = [False]*N
for _ in range(N):
    s, b = map(int, input().split())
    S[_] = s
    B[_] = b
ans = abs(S[0]-B[0])
def backtracking(Smul,Bsum,depth):
    global ans
    if depth > 0:
        ans = min(ans,abs(Smul-Bsum))
    for i in range(N):
        if used[i]:
            continue
        used[i] = True
        backtracking(Smul*S[i],Bsum+B[i],depth+1)
        used[i] = False

backtracking(1,0,0)
print(ans)
    