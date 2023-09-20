
##Idea - 02468 => ZWUXG 고유문자
def sol4(string1): 
    ans = [0 for _ in range(10)]
    keyword = 'ZOWRUFXSGI'
    kdict = {keyword[X]:X for X in range(len(keyword))}
    for s in string1:
        if s in keyword:
            ans[kdict[s]] += 1
    ans[1] = ans[1] - ans[0] - ans[2] - ans[4]
    ans[3] = ans[3] - ans[0] - ans[4]
    ans[5] = ans[5] - ans[4]
    ans[7] = ans[7] - ans[6]
    ans[9] = ans[9] - ans[5] - ans[6] - ans[8]
    buffer = ''
    for idx, i in enumerate(ans):
        buffer += str(idx)*i
    return buffer

for tc in range(1,int(input())+1):
    print(f'Case #{tc}: {sol4(input())}')
