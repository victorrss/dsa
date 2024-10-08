class Solution:
    def valid(self, grid, x, y, prevPos):
        n = len(grid)
        return x >= 0 and x <= n - 1 and y >= 0 and y <= n - 1 and prevPos + 1 == grid[x][y]

    def walkKnight(self, walkQty, target, grid, prevPos, x, y):
        if walkQty == target:
            return True
        
        dx = [2, 1, -1, -2, -2, -1, 1, 2]
        dy = [1, 2, 2, 1, -1, -2, -2, -1]
        mov = 0

        while mov < 8:
            nx = x + dx[mov]
            ny = y + dy[mov]

            if self.valid(grid, nx, ny, prevPos):
                return self.walkKnight(walkQty + 1, target, grid, grid[nx][ny], nx, ny)
            mov += 1
        return False

    def checkValidGrid(self, grid: List[List[int]]) -> bool:
        allNums = []
        for nums in grid:
            allNums.extend(nums)

        target = max(allNums)

        return self.walkKnight(0, target, grid, grid[0][0], 0, 0)
