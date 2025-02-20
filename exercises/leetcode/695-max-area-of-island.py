class Solution:
    def validPosition(self, x, y, grid):
        rows = len(grid)
        cols = len(grid[0])
        return 0 <= x < rows and 0 <= y < cols

    # TC: O(m*n)
    # SC: O(m*n)
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(x, y):
            if not self.validPosition(x, y, grid) or grid[x][y] != 1:
                return 0

            grid[x][y] = 0  # visited
            area = 1

            for i, j in directions:
                xi, yj = x + i, y + j
                area += dfs(xi, yj)

            return area

        max_area = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    max_area = max(max_area, dfs(x, y))

        return max_area
