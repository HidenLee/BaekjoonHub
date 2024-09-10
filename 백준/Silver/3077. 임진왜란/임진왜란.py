N = int(input())
dic = { elm : idx for idx, elm in enumerate(list(input().split()))}
cnt = 0
ipt = list(input().split())
for idx in range(N-1):
    for jdx in range(idx+1,N):
        if dic[ipt[idx]] < dic[ipt[jdx]]:
            cnt += 1
ans = str(cnt) + "/" + str((N*(N-1))//2)
print(ans)
