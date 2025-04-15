from collections import defaultdict
from sys import stdin
input = stdin.readline

N = int(input())
A = [0]*N
B = [0]*N
C = [0]*N
D = [0]*N
for _ in range(N):
    A[_],B[_],C[_],D[_] = map(int,input().split())
AB = defaultdict(int)
for a in A:
    for b in B:
        AB[a+b] += 1
ans = 0
for c in C:
    for d in D:
        if -(c+d) in AB.keys():
            ans += AB[-(c+d)]
print(ans)

