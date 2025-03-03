class Solution:
    def validPos(self, x, y, grid):
        r = len(grid)
        c = len(grid[0])
        return 0 <= x < r and 0 <= y < c

    def orangesRotting(self, grid: List[List[int]]) -> int:
        CONST_FRESH = 1
        CONST_ROTTEN = 2
        fresh = 0
        times = 0
        queue = deque([])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == CONST_FRESH:
                    fresh += 1
                if grid[x][y] == CONST_ROTTEN:
                    queue.append((x, y))

        while fresh > 0 and queue:
            all_in_the_level = len(queue)
            for _ in range(all_in_the_level):
                x, y = queue.popleft()
                for i, j in directions:
                    xi, yj = x + i, y + j
                    if self.validPos(xi, yj, grid) and grid[xi][yj] == CONST_FRESH:
                        grid[xi][yj] = CONST_ROTTEN
                        queue.append((xi, yj))
                        fresh -= 1
            times += 1

        return times if fresh == 0 else -1
