def solution(arrows):
    delta = [(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1)]
    
    points = set()
    edges = set()
    ox, oy = 0, 0
    points.add((ox,oy))

    for d in arrows:
        for _ in range(2):  
            nx = ox + delta[d][0]*0.5
            ny = oy + delta[d][1]*0.5

            edges.add(((ox,oy),(nx,ny)))
            edges.add(((nx,ny),(ox,oy)))
            points.add((nx,ny))
            ox, oy = nx, ny

    return len(edges) // 2 - len(points) + 1