# https://www.acmicpc.net/problem/2637
from collections import deque
N = int(input())
cnt = [0] * (N+1) #진입차수
require = [[] for _ in range(N+1)] # input 저장
needs = [[0]*(N+1) for _ in range(N+1)] # 계산 배열
for _ in range(int(input())):
    X, Y, K = map(int,input().split())
    require[Y].append((X,K))
    cnt[X] += 1

stack = deque([])
for i in range(1,N+1):
    if cnt[i] == 0 :
        stack.append(i)
        needs[i][i] = 1

while stack:
    now = stack.pop()
    for nxt_part, nxt_amount in require[now]:
        for i in range(1,N+1):
            needs[nxt_part][i] += needs[now][i] * nxt_amount 
        cnt[nxt_part] -= 1
        if cnt[nxt_part] == 0:
            stack.appendleft(nxt_part)
for i in range(1,N+1):
    if needs[N][i] > 0:
        print(i, needs[N][i])