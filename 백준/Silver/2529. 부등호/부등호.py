# https://www.acmicpc.net/problem/2529

N = int(input())
isBig = [True if char == "<" else False for char in map(str,input().split())]
usedd = [False for _ in range(10)]
big = ""
small = ""
def backtracking(now,used):
    global big, small
    size = len(now)
    if size == N + 1:
        if small == "":
            small = now
        else:
            big = now
        return
    for n in range(10):
        if used[n]:
            continue
        if size == 0 or ((int(now[size-1]) < n) == isBig[size-1]):
            used[n] = True
            backtracking(now + str(n),used)
            used[n] = False
backtracking("",usedd)
print(big)
print(small)