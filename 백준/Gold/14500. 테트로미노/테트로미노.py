# Input grid dimensions
N, M = map(int, input().split())

# Define the basic tetromino shapes
shapes = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # I shape, horizontal
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # I shape, vertical
    [(0, 0), (0, 1), (1, 0), (1, 1)],  # O shape
    [(0, 0), (1, 0), (2, 0), (2, 1)],  # L shape
    [(0, 0), (1, 0), (1, 1), (1, 2)],  # L shape rotated
    [(0, 0), (0, 1), (1, 1), (2, 1)],  # T shape
    [(0, 1), (1, 0), (1, 1), (1, 2)],  # T shape rotated
    [(0, 0), (1, 0), (1, 1), (2, 1)],  # Z shape
    [(0, 1), (1, 0), (1, 1), (2, 0)]   # Z shape mirrored
]

# Generate all rotations and flips
tetrominoes = set()
for shape in shapes:
    for rotation in [[(x, y) for x, y in shape], [(y, -x) for x, y in shape], [(-x, -y) for x, y in shape], [(-y, x) for x, y in shape]]:
        sorted_rotation = tuple(sorted(rotation))
        tetrominoes.add(sorted_rotation)

# Convert tetrominoes to list
tetrominoes = [list(shape) for shape in tetrominoes]

# Input grid values
table = [list(map(int, input().split())) for _ in range(N)]
ans = 0

# Traverse each cell in the grid
for x in range(N):
    for y in range(M):
        for tetro in tetrominoes:
            temp_sum = 0
            valid = True
            for dx, dy in tetro:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    temp_sum += table[nx][ny]
                else:
                    valid = False
                    break
            if valid:
                ans = max(ans, temp_sum)

print(ans)