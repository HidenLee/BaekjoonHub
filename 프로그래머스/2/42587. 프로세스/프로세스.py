def solution(priorities, location):
    from collections import deque
    dq = deque(enumerate(priorities))
    count = 0
    while dq:
        temp = dq.popleft()
        if any([temp[1] < x[1] for x in dq]):
            dq.append(temp)
        else:
            count += 1
            if temp[0] == location:
                return count
