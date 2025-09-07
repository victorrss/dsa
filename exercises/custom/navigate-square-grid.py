def print_grid(grid):
    for linha in grid:
        print(" ".join(linha))

def validPos(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def is_vertice(x, y):
    return abs(x) == 2 and abs(y) == 2

def is_center(x, y):
    return x == 0 and y == 0

def change_square_neighbours(grid, i, j):
    directions = []
    for x in range(-2, 3):
        for y in range(-2, 3):
            if not is_vertice(x, y) and not is_center(x, y):
                directions.append((x, y))

    for x, y in directions:
        dx, dy = i + x, j + y
        if validPos(grid, dx, dy):
            grid[dx][dy] = "@"

# Example using a grid 7x7
grid = [["." for _ in range(7)] for _ in range(7)]

# Set the start point
grid[3][3] = "X"

# Print before
print_grid(grid)

print("\n-----------------------\n")

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "X":
            change_square_neighbours(grid, i, j)

# Print after
print_grid(grid)

# #output
# . . . . . . .
# . . . . . . .
# . . . . . . .
# . . . X . . .
# . . . . . . .
# . . . . . . .
# . . . . . . .

# -----------------------

# . . . . . . .
# . . @ @ @ . .
# . @ @ @ @ @ .
# . @ @ X @ @ .
# . @ @ @ @ @ .
# . . @ @ @ . .
# . . . . . . .
