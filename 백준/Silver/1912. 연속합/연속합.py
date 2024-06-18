# https://www.acmicpc.net/problem/1912
n = int(input())
arr = list(map(int,input().split()))

dp = [arr[0] for _ in range(n)]
ans = arr[0]
for idx in range(1,n):
    dp[idx] = max(arr[idx],dp[idx-1]+arr[idx])
    if ans < dp[idx]:
        ans = dp[idx]
# print(max(dp))
print(ans)

