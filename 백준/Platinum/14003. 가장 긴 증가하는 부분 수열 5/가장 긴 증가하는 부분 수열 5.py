from bisect import bisect_left
N = int(input())
arr = [0] + list(map(int,input().split()))
dp = [10**10+1] * (N+1)
idxs = [0] * (N+1)
cnt = 0
for idx in range(1,N+1):
    jdx = bisect_left(dp,arr[idx],1)
    cnt = max(jdx,cnt)
    dp[jdx] = arr[idx]
    idxs[idx] = jdx

target = cnt
ans = []
for kdx in range(N,0,-1):
    if idxs[kdx] == target:
        ans.append(arr[kdx])
        target -= 1
print(cnt)
print(*ans[::-1])
