for _ in range(int(input())):
    W, N = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dist = 0
    now_idx = 0
    buffer = W
    for x, w in arr:
        if buffer > w:
            dist += x - now_idx
            now_idx = x
            buffer -= w
        elif buffer == w:
            dist += x - now_idx + x
            now_idx = 0
            buffer = W
        else:
            dist += x-now_idx + x + x
            now_idx = x
            buffer = W - w
    print(dist + now_idx)