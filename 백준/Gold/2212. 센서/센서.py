N = int(input())
K = int(input())
dist = [0]*N
old = 0
idx = 0
for i in sorted(list(map(int,input().split()))):
    dist[idx] = i - old
    idx += 1
    old = i
print(sum(sorted(dist[1:])[:N-K]))
# 1696367
# 123 678910
# 3456789 1