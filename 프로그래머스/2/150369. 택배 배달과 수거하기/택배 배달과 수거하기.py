def solution(cap, n, deliveries, pickups):
    answer = 0
    caps = [0,0]
    for i in range(n):
        if deliveries[n-1-i] == 0 and pickups[n-1-i] == 0:
            continue
        count = 0
        while caps[0] < deliveries[n-1-i] or caps[1] < pickups[n-1-i]:
            count += 1
            caps[0] += cap
            caps[1] += cap
        caps[0] -= deliveries[n-1-i]
        caps[1] -= pickups[n-1-i]
        answer += count*2*(n-i)
    return answer

