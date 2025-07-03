def solution(money):
    def count(arr):
        answer = 0
        dp = [[0,0] for _ in range(len(arr))]
        dp[0][1] = arr[0]
        for i in range(1,len(arr)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1])
            dp[i][1] = max(dp[i-1][1],dp[i-1][0] + arr[i])
        return max(dp[-1])
    return max(count(money[1:]),count(money[:-1]))