import heapq
for _ in range(int(input())):
    maxHeap = []
    minHeap = []
    visit = set()
    for idx in range(int(input())):
        cmd, num = tuple(input().split())
        num = int(num)
        if cmd == "I":
            heapq.heappush(minHeap,(num,idx))
            heapq.heappush(maxHeap,(-num,idx))
        elif cmd == "D":
            if num == -1:  
                while minHeap and minHeap[0][1] in visit:
                    heapq.heappop(minHeap)
                if minHeap:
                    visit.add(heapq.heappop(minHeap)[1])
            elif num == 1:
                while maxHeap and maxHeap[0][1] in visit:
                    heapq.heappop(maxHeap)
                if maxHeap:
                    visit.add(heapq.heappop(maxHeap)[1])
    while minHeap and minHeap[0][1] in visit:
        heapq.heappop(minHeap)
    while maxHeap and maxHeap[0][1] in visit:
        heapq.heappop(maxHeap)

    if minHeap and maxHeap:
        print(-maxHeap[0][0], minHeap[0][0])
    else:
        print("EMPTY")