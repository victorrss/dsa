class Solution:
    def validPosition(self, x, y, rooms):
        rows = len(rooms)
        cols = len(rooms[0])
        return 0 <= x < rows and 0 <= y < cols
    
    # TC: O(NxM)
    # SC: O(NxM)
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        INF = 2147483647
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        queue = deque([])

        # add all gates in the queue
        for x in range(len(rooms)):
            for y in range(len(rooms[0])):
                if rooms[x][y] == 0:
                    queue.append((x, y))

        # BFS to find the min path
        while queue:
            x, y = queue.popleft()
            for i, j in directions:
                xi, yj = x + i, y + j
                if self.validPosition(xi, yj, rooms) and rooms[xi][yj] == INF:
                    rooms[xi][yj] = rooms[x][y] + 1
                    queue.append((xi, yj))
