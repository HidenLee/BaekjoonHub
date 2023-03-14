T = int(input())
window = [0 for _ in range(42)]
window[0] = (1,0)
window[1] = (0,1)
for test_case in range(T):
    N = int(input())
    if window[N]:
        print(*window[N])
        continue
    else:
        idx = 1
        while idx <= N:
            idx += 1
            if not window[idx]:
                window[idx] = ((window[idx-2][0]+window[idx-1][0],window[idx-2][1]+window[idx-1][1]))
        print(*window[N])
