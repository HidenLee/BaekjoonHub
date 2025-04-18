delta = [(-1,0),(1,0),(0,-1),(0,1)]
for _ in range(int(input())):
    h, w = map(int, input().split())
    arr = [list(input()) for _ in range(h)]
    keys = set([i.upper() for i in list(input())])
    keys.update([".","$"])
    visit = set()
    doors = {chr(i): [] for i in range(65, 91)} # A-Z
    ans = 0
    stack = []
    for x in range(h):
        for y in range(w):
            if x == 0 or y == 0 or x == h-1 or y == w-1:
                if arr[x][y] != "*":
                    stack.append((x, y))
                    visit.add((x, y))
    while stack:
        x,y = stack.pop()
        elm = arr[x][y]
        if elm == "$":
            ans += 1
            arr[x][y] = "."

        elif elm.islower():
            key = elm.upper()
            if key not in keys:
                keys.add(key)
                for dx,dy in doors[key]:
                    if (dx,dy) not in visit:
                        stack.append((dx,dy))
                        visit.add((dx,dy))
                doors[key] = []
            
        elif elm.isupper():
            if elm not in keys:
                doors[elm].append((x,y))
                visit.remove((x,y))
                continue

    
        for dx,dy in delta:
            nx,ny = x+dx,y+dy
            if 0 <= nx < h and 0 <= ny < w and arr[nx][ny] != "*" and (nx,ny) not in visit:
                stack.append((nx,ny))
                visit.add((nx,ny))
    print(ans)