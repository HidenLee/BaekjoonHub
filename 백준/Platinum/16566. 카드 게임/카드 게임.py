from bisect import bisect_left
from bisect import bisect_right
N, M, K = map(int,input().split())
blue = sorted(map(int,input().split()))

ref = list(range(N))

def find(n):
    if ref[n] != n:
        ref[n] = find(ref[n])
    return ref[n]
for red in map(int,input().split()):

    i = find(bisect_right(blue,red))
    print(blue[i])
    ref[i] = i + 1    
