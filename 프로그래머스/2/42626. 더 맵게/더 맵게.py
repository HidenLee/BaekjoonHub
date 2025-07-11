def solution(scoville, K):
    import heapq
    answer = 0
    heapq.heapify(scoville)
    while len(scoville) >= 2:
        lowest = heapq.heappop(scoville)
        if lowest >= K:
            return answer
        heapq.heappush(scoville,lowest+heapq.heappop(scoville)*2)
        answer += 1
    return -1 if scoville[0] < K else answer