def solution(bridge_length, weight, truck_weights):
    from collections import deque
    
    bridge = deque([0 for _ in range(bridge_length)])
    trucks = deque(truck_weights)
    answer = 0
    now = weight
    while bridge and trucks:
        answer += 1
        now += bridge.popleft()
        
        if trucks and trucks[0] <= now:
            now -= trucks[0]
            bridge.append(trucks.popleft())
            continue
        else:
            bridge.append(0)
    remain = 0
#     for idx in range(bridge_length-1,-1,-1):
#         if bridge[idx]:
#             remain = idx + 1
#             break
    
    return answer + remain + bridge_length