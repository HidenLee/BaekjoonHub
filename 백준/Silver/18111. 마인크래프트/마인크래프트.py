N, M, B = map(int, input().split())
min_height = 0
max_height = 256
MAX_VAL = 256 * N * M * 2
land = [[0] * M for _ in range(N)]
total = 0
for idx in range(N):
    ipt = tuple(map(int, input().split()))
    for jdx,elm in enumerate(ipt):
        land[idx][jdx] = elm
    max_height = max(max_height, max(ipt))
    min_height = min(min_height, min(ipt))
    total += sum(ipt)
min_cost = MAX_VAL
def flattening(target):
    if total + B < target * N * M:
        return MAX_VAL
    cost = 0
    for i in range(N):
        for j in range(M):
            temp = (land[i][j] - target) * 2 if land[i][j] >= target else target - land[i][j]
            cost += temp
            if cost > min_cost:
                return MAX_VAL
    return cost
    


for target in range(min_height, max_height + 1):
    temp = flattening(target)
    if min_cost >= temp:
        min_cost = temp
        max_height = target
        
print(min_cost, max_height)