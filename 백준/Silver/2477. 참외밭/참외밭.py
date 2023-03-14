K = int(input())
d = [[] for _ in range(5)]
temp = 0
V = [0]*5
ipt = [list(map(int,input().split())) for _ in range(6)]
for _ in range(6):
    ipt.append(ipt[_])
for idx in range(len(ipt)-3):
    if ipt[idx][0] == ipt[idx+2][0] and ipt[idx+1][0] == ipt[idx+3][0]:
        small =  ipt[idx+1][1] * ipt[idx+2][1]
        temp = (ipt[idx][0],ipt[idx+1][0])
        break
big = ([x[1] for x in ipt if not x[0] in temp])
big = min(big) * max(big)
print(K*(big-small))
