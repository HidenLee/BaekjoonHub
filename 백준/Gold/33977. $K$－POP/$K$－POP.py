import math
K = int(input())
x= math.floor(math.sqrt(K)) 
while 1 < x:
    if not  K % x:
        break
    x -= 1
N = x + K//x
print(N)
now = 1
if N > 2*x - 1:
    for _ in range(N - (2*x-1)):
        print(now, now+1)
        now += 1
    while now < N:
        print(now, now+1)
        print(now, now+2)
        now += 2