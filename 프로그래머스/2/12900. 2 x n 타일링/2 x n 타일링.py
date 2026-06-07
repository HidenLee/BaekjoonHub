def solution(n):
    dp = [1,2]
    while len(dp) < n:
        dp.append((dp[-1]+dp[-2])% 1000000007)
    return dp[n-1] % 1000000007

def solution1(n):
    dp = [1 for _ in range(60001)]
    dp[1] = 2
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n-1] % 1000000007
