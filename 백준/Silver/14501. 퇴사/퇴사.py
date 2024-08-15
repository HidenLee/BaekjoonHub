# https://www.acmicpc.net/problem/14501

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
maxearn = [0]*(N+1)

stack = [(0,0)]
while stack:
    day, earn = stack.pop()
    maxearn[day] = max(maxearn[day],earn)
    if day == N :
        continue
    if day + 1 <= N:
        stack.append((day+1,earn))
    if day+arr[day][0] <= N:
        stack.append((day+arr[day][0],earn+arr[day][1]))
print(maxearn[-1])