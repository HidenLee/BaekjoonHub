# https://www.acmicpc.net/problem/1654 랜선 자르기

K, N = map(int, input().split())

lst = []
mx = 0
for _ in range(K):
    ipt = int(input())
    lst.append(ipt)
    mx = max(mx,ipt)
mn = 1
while True:
    md = (mx + mn) // 2
    cnt = sum([i // md for i in lst])

    if cnt < N:
        mx = md - 1
    else:
        mn = md + 1
    if mx < mn:
        print(mx)
        break    
