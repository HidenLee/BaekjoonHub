N, X = map(int, input().split())
dic = {}
import math
for _ in range(N):
    A, B, C, T = map(int, input().split())
    high = T + math.ceil(C / A) 
    highValue = (high-T) * A
    if highValue < X :
        continue
    start = T + math.ceil(X / A)
    # highValue - B * (end-high) < X
    end = high + math.floor((highValue-X) / B)  
    if start in dic:
        dic[start] += 1
    else:
        dic[start] = 1

    if end+1 in dic:
        dic[end+1] -= 1
    else:
        dic[end+1] = -1

local = 0
ans = 0
past  = 0
for key in sorted(dic.keys()):
    temp = local
    local += dic[key]
    if temp >= 3:
        ans += key - past
    past = key
print(ans)

