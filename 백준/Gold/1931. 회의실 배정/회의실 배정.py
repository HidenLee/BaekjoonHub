N = int(input())
table = sorted([tuple(map(int,input().split())) for _ in range(N)],key=lambda x: (x[1],x[0]) )
answer = 0
now = -1
for s,e in table:
    if s < now:
        continue
    answer += 1
    now = e
print(answer)