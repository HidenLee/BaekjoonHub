N,M =map(int,input().split())
arr = {}
left = 1
right = 0
for _ in range(M):
    a,b,c = map(int,input().split())
    # if a in arr:
    #     arr[a] = (b,min(arr[a][1],c))
    # else:
    #     arr[a] = (b,c)
    # if b in arr:
    #     arr[b]=  (a,min(arr[b][1],c))
    # else:
    #     arr[b] = (a,c)
    if a not in arr:
        arr[a] = []
    if b not in arr:
        arr[b] = []
    arr[a].append((b, c))
    arr[b].append((a, c))
    right = max(right,c)

s,e = map(int,input().split())


from collections import deque

def is_transportable(weight):
    visited = set()
    queue = deque([s])
    visited.add(s)
    
    while queue:
        current = queue.popleft()
        
        if current == e:
            return True
        
        for neighbor, capacity in arr.get(current, []):
            if neighbor not in visited and capacity >= weight:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return False

def findMinWeight(left,right):
    result = left
    while left <= right:
        mid = (left + right) // 2
        
        if is_transportable(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result

print(findMinWeight(left,right))