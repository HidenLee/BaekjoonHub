def cross(a,b):
    return (a[0]*b[1] - a[1]*b[0]) / 2.0

N = int(input())
ans = 0
table = [tuple(map(int,input().split())) for _ in range(N)]
while N != 0:
    ans += cross(table[N-1],table[N-2])
    N -= 1
print(abs(ans))