def solution(book_time):
    import heapq
    answer = 0
    stack = []
    for st, ed in sorted([list(map(lambda x: (60*int(x[:2])+int(x[3:])),y)) for y in book_time],key=lambda x:-x[1]):
        print(st,ed)
        if stack:
            compare = - heapq.heappop(stack)
            if ed  <= compare:
                heapq.heappush(stack,-st+10)
            else:
                heapq.heappush(stack,-compare)
                heapq.heappush(stack,-st+10)
                
        else:
            heapq.heappush(stack,-st+10)
        answer = max(answer,len(stack))    
    return answer