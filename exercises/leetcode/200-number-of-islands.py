# Kruskal Algo
class Solution:
    def find(self, x, id):
        if x == id[x]:
            return x
        group = self.find(id[x], id)
        id[x] = group
        return group

    def union(self, x, y, id):
        id[self.find(x, id)] = self.find(y, id)

    def isValidPos(self, x, y, matrix):
        return 0 <= x < len(matrix) and 0 <= y < len(matrix[x])

    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]]
        n = len(grid)
        m = len(grid[0])
        ids = [0] * (n * m)

        for i in range(n):
            for j in range(m):
                idx = i * m + j
                ids[idx] = idx

        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    for d in directions:
                        x = i + d[0]
                        y = j + d[1]
                        if not self.isValidPos(x, y, grid):
                            continue

                        if grid[x][y] == "1":
                            id1 = i * m + j
                            id2 = x * m + y
                            self.union(id1, id2, ids)

        count = 0
        for i in range(n):
            for j in range(m):
                idx = i * m + j
                if grid[i][j] == "1" and self.find(idx, ids) == idx:
                    count += 1
        return count
