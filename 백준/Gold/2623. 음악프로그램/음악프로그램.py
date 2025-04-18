N, M = map(int, input().split())
ans = [0] * (N)
dic = {x:set() for x in range(1, N+1)}
for _ in range(M):
    ipt = tuple(map(int, input().split()))
    for idx in range(1, ipt[0]):
        dic[ipt[idx+1]].add(ipt[idx])
cnt = N
while cnt > 0:
    for idx in range(1, N+1):
        if len(dic[idx]) == 0:
            ans[N-cnt] = idx
            dic[idx].add(0)
            cnt -= 1
            for jdx in range(1, N+1):
                if idx in dic[jdx]:
                    dic[jdx].remove(idx)
            break
    else:
        print(0)
        exit()
print(*ans, sep="\n")