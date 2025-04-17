table = [[0]*9 for _ in range(9)]
zeros = []
for idx in range(9):
    ipt = list(input())
    for jdx,elm in enumerate(ipt):
        if elm == "0":
            zeros.append((idx,jdx))
        table[idx][jdx] = int(elm)
def check(x,y,num):
    for i in range(9):
        if table[x][i] == num:
            return False
        if table[i][y] == num:
            return False
    x = (x//3)*3        
    y = (y//3)*3
    for i in range(3):
        for j in range(3):
            if table[x+i][y+j] == num:
                return False
    return True

def solve(idx):
    if idx == len(zeros):
        for _ in range(9):
            print(sum([elm*10**(8-idx) for idx,elm in enumerate(table[_])]))
        exit()
    x, y = zeros[idx]
    for num in range(1, 10):
        if check(x,y,num):
            table[x][y] = num
            solve(idx + 1)
            table[x][y] = 0

solve(0)