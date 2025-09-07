def solution(line):  
    def cross(line1,line2):
        A,B,E = line1
        C,D,F = line2
        if A*D == B*C:
            return (False,False)
        x, xd = divmod(B*F-E*D,A*D-B*C)
        if xd: return (False,False)
        y, yd = divmod(E*C-A*F,A*D-B*C)
        if yd: return (False,False)
        return (x,y)
    dots = set()
    minx = miny = 10e9
    maxx = maxy = -10e9
    for i in range(len(line)-1):
        for j in range(i+1,len(line)):
            x,y = cross(line[i],line[j])
            if type(x) == bool:
                continue
            minx = min(x,minx)
            miny = min(y,miny)
            maxx = max(x,maxx)
            maxy = max(y,maxy)
            dots.add((x,y))
    # print(list(dots))
    # print(minx,miny,maxx,maxy)
    table = [["." for _ in range(maxx-minx+1)] for _ in range(maxy-miny+1)]
    for x, y in dots:
        table[y-miny][x-minx] = "*"
    return ["".join(table[-i-1]) for i in range(len(table))]