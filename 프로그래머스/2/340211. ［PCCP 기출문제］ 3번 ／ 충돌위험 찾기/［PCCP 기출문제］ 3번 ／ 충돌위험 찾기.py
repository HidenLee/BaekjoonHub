def solution(points, routes):
    points = [[]] + points
    minimap = [[set() for _ in range(100)] for _ in range(100)]
    colision = set()
    
    def updateSet(r,c,t):
        if t in minimap[r-1][c-1]:
            if (r,c,t) not in colision:
                colision.add((r,c,t))
        else:
            minimap[r-1][c-1].add(t)
    
    for idx, robot in enumerate(routes):
        time = 0
        org = robot[0]
        oR, oC = points[org][0], points[org][1]
        updateSet(oR,oC,time)
        for nxt in robot[1:]:
            nR, nC = points[nxt][0], points[nxt][1]
            while oR != nR or oC != nC:
                if oR < nR:
                    oR += 1
                elif oR > nR:
                    oR -= 1
                elif oC < nC:
                    oC += 1
                elif oC > nC:
                    oC -= 1
                time += 1
                updateSet(oR,oC,time)
    return len(colision)