import heapq
def solution(cards):
    cards = [0] + cards
    visited = [False for _ in range(len(cards))]
    answer = [0]
    for idx, elm in enumerate(cards):
        if visited[idx] or idx == 0:
            continue
        count = 0
        while not visited[idx]:
            visited[idx] = True
            idx = cards[idx]
            count += 1
        heapq.heappush(answer,-count)
    return heapq.heappop(answer) * heapq.heappop(answer)