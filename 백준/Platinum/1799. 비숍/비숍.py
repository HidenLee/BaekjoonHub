N = int(input())

table = []
odd = []
even = []
for idx in range(N):
    ipt = map(int,input().split())
    for jdx, elm in enumerate(ipt):
        if elm == 1:
            if (idx+jdx) % 2 :
                odd.append((idx,jdx))
            else:
                even.append((idx,jdx))
    table.append(ipt)

def backtrack(arr):
    max_cnt = 0
    stack = [(0,0,set(),set())]

    while stack:
        idx, cnt, NE, SE = stack.pop() # North-east mean  "/" whiie South-east mean "\"

        if idx == len(arr):
            max_cnt = max(max_cnt,cnt)
            continue
        temp = (arr[idx][0] + arr[idx][1], arr[idx][0] - arr[idx][1])
        if temp[0] not in NE and temp[1] not in SE:
            new_NE = NE.copy()
            new_SE = SE.copy()
            new_NE.add(temp[0])
            new_SE.add(temp[1])
            stack.append((idx + 1, cnt + 1, new_NE, new_SE))

        stack.append((idx+1,cnt,NE,SE))

    return max_cnt

print(backtrack(even) + backtrack(odd))



        