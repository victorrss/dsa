"""
2D Grid – Count Lakes Inside an Island

You are given a 2D grid where:

'X' represents land

'.' represents water

You are also given a starting coordinate (sr, sc) that is guaranteed to lie on land. Consider the island that is 4-directionally connected to (sr, sc) (up, down, left, right). Your task is to count how many lakes are inside this island.

A lake is a maximal 4-directionally connected region of '.' (water) that does not touch the outer boundary of the grid (i.e., it’s completely surrounded by 'X' land). Water connected to the grid’s outer border is considered ocean and does not count.

Return the number of such lakes.

Rules & Notes

Connectivity is 4-directional only.

Only count lakes that lie inside the island containing (sr, sc). Water outside the island (i.e., adjacent to land not reachable from (sr, sc)) should not be counted even if it’s enclosed elsewhere.

The start is always valid land: grid[sr][sc] == 'X'.

Constraints

1 <= rows, cols <= 500

grid[r][c] ∈ {'X', '.'}

0 <= sr < rows, 0 <= sc < cols

grid[sr][sc] == 'X'

Examples
Example 1

Input

grid = [
  ["X","X","X"],
  ["X","X","X"],
  ["X","X","X"]
]
start = (1, 1)


Output

0


Explanation: No water cells at all.

Example 2

Input

grid = [
  ["X","X","X","X","X"],
  ["X",".",".","X","X"],
  ["X",".","X","X","X"],
  ["X","X","X","X","X"],
]
start = (2, 2)


Output

1


Explanation: The two '.' on the left are connected and fully enclosed by land → 1 lake.

Example 3

Input

grid = [
  [".",".",".",".",".",".","."],
  [".","X","X","X","X","X","."],
  [".","X",".","X",".","X","."],
  [".","X",".","X",".","X","."],
  [".","X","X","X","X","X","."],
  [".",".",".",".",".",".","."],
]
start = (2, 1)


Output

2


Explanation: The outer border is ocean. Inside the central land island there are two enclosed water regions (left pocket and right pocket), each a lake.

Example 4 (water touching border ≠ lake)

Input

grid = [
  ["X","X","X","X"],
  ["X",".","X","."],
  ["X","X","X","X"],
]
start = (1, 0)


Output

0


Explanation: The water on the right touches the grid border via the top edge, so it’s ocean.

Approach

Find the island connected to (sr, sc):

Run BFS/DFS from (sr, sc) over 'X' cells.

Store all land coordinates of this island in a set island.

Count lakes inside that island:

Iterate over all cells; when you find an unvisited '.', run BFS/DFS over water.

Track whether this water component touches the grid border. If it does, it’s ocean.

Also ensure this water lies inside the island’s boundary. (In practice, if water touches the grid border it’s ocean; otherwise, if fully enclosed by land, it’s a lake.)

Increment count for each enclosed water component.

Time Complexity: O(R*C) (each cell visited O(1) times across the searches)
Space Complexity: O(R*C) for visited sets/queues
"""
# Reference Implementation (Python)
from collections import deque

def count_lakes(grid, start):
    rows, cols = len(grid), len(grid[0])
    (sr, sc) = start

    # 1. BFS para encontrar a ilha (terra conectada)
    visited = set()
    q = deque([(sr, sc)])
    island = set()
    
    while q:
        r, c = q.popleft()
        if (r, c) in visited:
            continue
        visited.add((r, c))
        
        if grid[r][c] != "X":
            continue
        
        island.add((r, c))
        
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "X":
                q.append((nr, nc))

    # 2. Procurar lagos (regiões de água cercadas por terra)
    seen_water = set()
    lakes = 0

    def bfs_water(sr, sc):
        q = deque([(sr, sc)])
        enclosed = True

        while q:
            r, c = q.popleft()
            if (r, c) in seen_water:
                continue
            seen_water.add((r, c))

            # Se a água toca a borda externa do grid, não é lago
            if r == 0 or r == rows-1 or c == 0 or c == cols-1:
                enclosed = False

            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == ".":
                    q.append((nr, nc))
        return enclosed

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "." and (r,c) not in seen_water:
                if bfs_water(r, c):
                    lakes += 1

    return lakes


# Exemplo com o seu grid (7 colunas x 6 linhas)
grid6 = [
  [".",".",".",".",".",".","."],
  [".","X","X","X","X","X","."],
  [".","X",".","X",".","X","."],
  [".","X",".","X",".","X","."],
  [".","X","X","X","X","X","."],
  [".",".",".",".",".",".","."],
]

print(count_lakes(grid6, (2,1)))  # esperado: 2
