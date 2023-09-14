# https://www.acmicpc.net/problem/1881 공바꾸기

N = int(input())
if N == 0:
    print(0)
else:
    lst = list(map(int,input().split()))

    box = []
    ans = 0
    for idx in range(N):
        if lst[idx] in box:
            continue
        
        ans += 1
        if len(box) < 4:
            box.append(lst[idx])
        elif idx < N-1:
            buffer = [x for x in box]
            for nxt in lst[idx+1:]:
                if nxt in buffer:
                    buffer.remove(nxt)
                    if len(buffer) == 1:
                        break
                # print('buffer',buffer) 
            box.remove(buffer[-1])
            box.append(lst[idx])
        else:
            if lst[idx] in box:
                ans += 1
        # print(box,ans)
    print(ans)

