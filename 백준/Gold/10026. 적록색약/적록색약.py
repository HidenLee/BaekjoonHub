from collections import deque

# Input reading
N = int(input())
arr = [[1 if x == "R" else 0 if x == "B" else -1 for x in list(input())] for _ in range(N)]

# Visit array to track visited cells for normal and color-blind vision
visit = [[False for _ in range(N)] for _ in range(N)]
visit_sick = [[False for _ in range(N)] for _ in range(N)]

# Directions for BFS
delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# BFS function
def bfs(x, y, is_colorblind):
    queue = deque([(x, y)])
    target_value = arr[x][y]
    
    # Mark the starting cell as visited
    if is_colorblind:
        visit_sick[x][y] = True
    else:
        visit[x][y] = True

    while queue:
        ox, oy = queue.popleft()
        
        for dx, dy in delta:
            nx, ny = ox + dx, oy + dy
            
            if 0 <= nx < N and 0 <= ny < N:
                # Normal vision BFS
                if not is_colorblind and not visit[nx][ny] and arr[nx][ny] == target_value:
                    visit[nx][ny] = True
                    queue.append((nx, ny))

                # Color-blind vision BFS
                if is_colorblind and not visit_sick[nx][ny]:
                    if (target_value in [1, -1] and arr[nx][ny] in [1, -1]) or (target_value == 0 and arr[nx][ny] == 0):
                        visit_sick[nx][ny] = True
                        queue.append((nx, ny))

# Counting regions for both normal and color-blind views
normal_count = 0
colorblind_count = 0

for i in range(N):
    for j in range(N):
        # Normal BFS
        if not visit[i][j]:
            bfs(i, j, is_colorblind=False)
            normal_count += 1
        
        # Color-blind BFS
        if not visit_sick[i][j]:
            bfs(i, j, is_colorblind=True)
            colorblind_count += 1

# Output results
print(normal_count, colorblind_count)