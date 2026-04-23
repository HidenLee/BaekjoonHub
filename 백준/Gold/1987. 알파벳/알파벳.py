# https://www.acmicpc.net/problem/1987
R, C = map(int, input().split())
board = [input() for _ in range(R)]
alphabets = set(''.join(board))
maxC = len(alphabets)
delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]
stack = [(0,0,1 << (ord(board[0][0]) - ord('A')), 1)]
answer = 1
while stack:
    oy, ox, mask, count = stack.pop()
    answer = max(answer, count)
    if answer == maxC:
        break
    for dy, dx in delta:
        ny, nx = oy + dy, ox + dx
        if 0 <= ny < R and 0 <= nx < C:
            nxtmask = 1 << (ord(board[ny][nx]) - ord('A'))
            if mask & nxtmask == 0:
                stack.append((ny, nx, mask | nxtmask, count + 1))
print(answer)        