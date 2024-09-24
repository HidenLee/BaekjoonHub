C, N = map(int,input().split())

import heapq
arr = []
for _ in range(N):
    cost,customer = map(int,input().split())
    efficiency = customer / cost
    arr.append((efficiency,cost,customer))

arr.sort(reverse=True,key=lambda X:X[0])
#     heapq.heappush(arr,(efficiency,cost,customer))

# index = 0
# now = 0
# ans = 0

# dp = [10e9] * (1001)
# dp[0] = 0


# import heapq

# C, N = map(int, input().split())

# arr = []
# for _ in range(N):
#     cost, customer = map(int, input().split())
#     arr.append((cost, customer))

pq = []
heapq.heappush(pq, (0, 0))  

visited = {}

while pq:
    ocost, ocustomers = heapq.heappop(pq)
    
    if ocustomers >= C:
        print(ocost)
        break
    
    if ocustomers in visited and visited[ocustomers] <= ocost:
        continue
    
    visited[ocustomers] = ocost
    
    for _,cost, customer in arr:
        next_cost = ocost + cost
        next_customers = ocustomers + customer
        
        if next_customers not in visited or visited[next_customers] > next_cost:
            heapq.heappush(pq, (next_cost, next_customers))