def solution(info, n, m):
    
    N = len(info)
    maxV = 3 * N + 1
    dp = [[maxV for _ in range(m)] for _ in range(N+1)]
    # dp[i][b] = B의 흔적 핪이 b일때, i-1까지 진행한 A의 최소 흔적
    dp[0][0] = 0
    for i in range(N):
        for b in range(m):
            if dp[i][b] == maxV:
                continue
            dp[i+1][b] = min(dp[i+1][b],dp[i][b]+info[i][0])
            if b + info[i][1] < m:
                dp[i+1][b+info[i][1]] = min(dp[i+1][b+info[i][1]],dp[i][b])
    minV = min(dp[N])
    return minV if minV < n else -1