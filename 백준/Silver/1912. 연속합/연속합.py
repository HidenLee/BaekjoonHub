# https://www.acmicpc.net/problem/1912
n = int(input())
arr = list(map(int,input().split()))
dp = [arr[0]]
for idx in range(1,n):
    dp.append(max(arr[idx],dp[idx-1]+arr[idx]))
print(max(dp))
