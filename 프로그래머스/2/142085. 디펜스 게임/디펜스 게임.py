import heapq
def solution(n, k, enemy):
    stack = []
    left = 0
    while left < len(enemy):
        heapq.heappush(stack,enemy[left])
        if len(stack) > k:
            n -= heapq.heappop(stack)
        if n < 0:
            return left
        left += 1

    return left