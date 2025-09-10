def solution(places):
    delta = [(0,1),(1,0),(0,-1),(-1,0)]
    def solve(place):
        for i in range(5):
            for j in range(5):
                if not place[i][j] == "P":
                    continue
                stack = [(i,j,0)]
                visit = set()
                visit.add(i*5+j)
                while stack:
                    oy, ox, cul = stack.pop()

                    if cul == 2:
                        continue
                    for dy,dx in delta:
                        ny, nx = dy+oy, dx+ox
                        if 0 <= ny < 5 and 0<= nx < 5 and place[ny][nx] != "X" and not ny*5+nx in visit:
                            visit.add(ny*5+nx)
                            stack.append((ny,nx,cul+1))
                            if place[ny][nx] == "P":
                                return 0
                            
        return 1
    return [solve(place) for place in places]