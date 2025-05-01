dic = {}
for tem, tmx in [map(int, input().split()) for _ in range(int(input()))]:
    if tem in dic:
        dic[tem] += 1
    else:
        dic[tem] = 1
    if tmx in dic:
        dic[tmx] -= 1
    else:
        dic[tmx] = -1
local = 0
ans = [0,0,0]
flag = False
for key in sorted(dic.keys()):
    local += dic[key]
    if local > ans[0]:
        ans[0] = local 
        ans[1] = key
        flag = True
    if local < ans[0] and flag:
        ans[2] = key
        flag = False
print(ans[0])
print(ans[1], ans[2])