def solution(m, n, startX, startY, balls):
    # answer = [((startX-(0-gx))**2+(startY-gy)**2,(startX-(2*m-gx))**2+(startY-gy)**2,(startY-(0-gy))**2+(startX-gx)**2,(startY-(n*2-gy))**2+(startX-gx)**2) for gx,gy in balls]
    answer = []
    for gx, gy in balls:
        temp =[]
        if not (startX > gx and startY == gy):
            temp.append((gx-(0-startX))**2+(startY-gy)**2)
        if not (startX < gx and startY == gy):
            temp.append((gx-(2*m-startX))**2+(startY-gy)**2)
        if not (startY > gy and startX == gx):
            temp.append((gy-(0-startY))**2+(startX-gx)**2)
        if not (startY < gy and startX == gx):
            temp.append((gy-(2*n-startY))**2+(startX-gx)**2)
        # if startX == startY < gx == gy:
        #     minV == min(minV,(startX+gx)**2+(startY+gy)**2)
        # if (m-startX) == (n-startY) < (m-gx) == (n-gy):
        #     minV == min(minV,(gy-(2*n-startY))**2+(gx-(2*m-startX))**2)
        answer.append(min(temp))
            
    return answer