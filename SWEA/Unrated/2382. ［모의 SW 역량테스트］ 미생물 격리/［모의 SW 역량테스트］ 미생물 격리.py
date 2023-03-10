T = int(input())
delta = {1: [-1, 0, 2], 2: [1, 0, 1], 3: [0, -1, 4], 4: [0, 1, 3]}
for test_case in range(1, T+1):
    N, M, K = map(int, input().split())
    micron = []
    for _ in range(K):
        y, x, size, direction = map(int, input().split())
        micron.append([y, x, size, direction])
    while M > 0:

        for idx in range(len(micron)):
            y, x, size, direction = micron[idx]
            y = y + delta[direction][0]
            x = x + delta[direction][1]
            if y == 0 or y == N - 1 or x == 0 or x == N - 1:
                size = size // 2
                direction = delta[direction][2]
            micron[idx] = [y, x, size, direction]

        nextstep = []
        for m in micron:
            if m[2]:
                if not (m[0], m[1]) in [(n[0], n[1]) for n in nextstep]:
                    nextstep.append([m[0], m[1], m[2], m[3]])
                else:
                    temp = [(n[2], n[3]) for n in micron if n[0] == m[0] and n[1] == m[1]]
                    # temp.append((m[2], m[3]))
                    temp.sort(key=lambda i: -i[0])
                    for idx in range(len(nextstep)):
                        if nextstep[idx][0] == m[0] and nextstep[idx][1] == m[1]:
                            nextstep[idx][2] = sum([n[0] for n in temp])
                            nextstep[idx][3] = temp[0][1]
                            break
        micron = nextstep
        M -= 1
    rst = sum([n[2] for n in micron])
    print(f'#{test_case} {rst}')
