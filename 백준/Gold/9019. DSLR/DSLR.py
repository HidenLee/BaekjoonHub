def D(n):
    return (2*n) % 10000
def S(n):
    return (10000 + n - 1) % 10000
def L(n):
    return (n % 1000) * 10 + (n // 1000)
def R(n):
    return (n % 10) * 1000 + (n // 10)

from collections import deque

N = int(input())
for _ in range(N):
    s, e = map(int,input().split())
    visited = [False for _ in range(10000)]
    deq = deque([("",s)])
    while deq:
        route, value = deq.popleft()
        if value == e:
            print(route)
            break
        for func, alp in [(D, "D"), (S, "S"), (L, "L"), (R, "R")]:
            if not visited[func(value)]:
                visited[func(value)] = True
                deq.append((route+alp,func(value)))
            
