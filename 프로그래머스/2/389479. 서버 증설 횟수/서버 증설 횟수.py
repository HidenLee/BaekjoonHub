def solution(players, m, k):
    import math
    servers = [0 for _ in range(24)]
    answer = 0
    for i in range(24):
        c = math.floor(players[i] / m)
        diff = c - servers[i]
        if diff <= 0:
            continue
        answer += diff
        for j in range(k):
            if i + j == 24:
                break
            servers[i+j] += diff
    return answer