def solution(board):
    count = [0,0]
    for i in range(3):
        for j in range(3):
            if board[i][j] == "O":
                count[0] += 1
            elif board[i][j] == "X":
                count[1] += 1

    print()
    if count[1] > count[0] or count[0] > count[1] + 1:
        return 0
    flagO = False
    flagX = False
    for a,b,c in [list(x) for x in board] + [[board[i][j] for i in range(3)] for j in range(3)] + [[board[i][i] for i in range(3)]] + [[board[2-i][i] for i in range(3)]]:
        if a==b==c=="O":
            flagO = True
        if a==b==c=="X":
            flagX = True
    if flagO and flagX:
        return 0
    if flagO and count[0] != count[1] + 1:
        return 0
    if flagX and count[0] != count[1]:
        return 0
    return 1