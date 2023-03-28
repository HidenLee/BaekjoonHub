N = int(input())
glass = [int(input()) for _ in range(N)]
glass = [0] + glass
sn = [0, glass[1]]
if N > 1:
    sn.append(glass[1]+glass[2])
idx = 3
while idx <= N: 
    temp = max(
        sn[idx-1],
        sn[idx-3] + glass[idx-1] + glass[idx],
        sn[idx-2] + glass[idx],
    )
    idx += 1
    sn.append(temp) 
print(sn[N])
