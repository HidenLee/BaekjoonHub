def solution(jobs):
    jobs.sort()
    import heapq
    time = 0
    leftidx = 0
    N = len(jobs)
    answer = []
    queue = []
    while len(answer) != N:
        while leftidx < N and jobs[leftidx][0] <= time:
            heapq.heappush(queue,(jobs[leftidx][1],jobs[leftidx][0],leftidx))
            leftidx += 1
        if not queue:
            time += 1
            continue
        duration, callTime, _ = heapq.heappop(queue)
        time += duration
        answer.append(time-callTime)

        
    return sum(answer) // N