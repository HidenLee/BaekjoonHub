def solution(n, works):
    import heapq
    works = [-x for x in works]
    heapq.heapify(works)
    while n > 0 and works:
        top = - heapq.heappop(works)
        if top:
            heapq.heappush(works,-top+1)
        n -= 1
    return sum([x**2 for x in works])