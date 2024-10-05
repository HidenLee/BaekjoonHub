N, K = map(int,input().split())
arr = list(input())
L = N - K
from collections import deque
deq = deque([])

for elm in arr:
    while len(deq) and K > 0 and deq[-1] < elm:
        deq.pop()
        K -= 1
    deq.append(elm)
print("".join(list(deq)[:L]))