import sys
ipt = sys.stdin.read().splitlines()

def root(node):
    while node != roots[node]:
        roots[node] = roots[roots[node]]  # Path compression
        node = roots[node]
    return node 

def union(start, end, depth):
    global ans
    start, end = root(start), root(end)
    if start == end:  # Cycle detected
        if ans == 0:  # Only capture the first cycle
            ans = depth
        return
    roots[max(start, end)] = min(start, end)  # Union operation
    

N, M = map(int, ipt[0].split())  # N is the number of nodes, M is the number of edges
ans = 0
roots = [x for x in range(N)]  # Initialize roots array

for idx in range(1, M + 1):
    start, end = map(int, ipt[idx].split())  # Parse the edge
    union(start - 1, end - 1, idx)  # Adjust for 0-based indexing

print(ans)
