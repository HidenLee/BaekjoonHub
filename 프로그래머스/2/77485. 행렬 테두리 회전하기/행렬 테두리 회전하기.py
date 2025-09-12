def solution(rows, columns, queries):
    table = [[j+1 for j in range(i*columns,(i+1)*columns)] for i in range(rows)]
    def solve(y1,x1,y2,x2):
        minV = prev = table[y1][x1]
        table[y1][x1] = 0
        for nx, ny in [(x1+i,y1) for i in range(1,x2-x1)] + [(x2,y1+i) for i in range(y2-y1)] + [(x2-i,y2) for i in range(x2-x1)] + [(x1,y2-i) for i in range(y2-y1)]:
            minV = min(minV,table[ny][nx])
            table[ny][nx], prev = prev, table[ny][nx]
        table[y1][x1] = prev
        minV = min(minV,prev)
        return minV    
    return [solve(x1-1,y1-1,x2-1,y2-1) for x1,y1,x2,y2 in queries]