class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if grid[0][0] == 1:
            return -1
        seen = {(0,0)}
        n = len(grid)
        queue = deque([(0, 0, 1)])
        directions = [(0, 1), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1), (0, -1), (-1, 0)]
        while queue:
            row, col, distance = queue.popleft()
            if (row, col) == (n-1, n-1):
                return distance
            for dr, dc in directions:
                newRow = row + dr
                newCol = col + dc
                if (0 <= newRow < n and 0 <= newCol < n and grid[newRow][newCol] == 0 and (newRow, newCol) not in seen):
                    seen.add((newRow, newCol))
                    queue.append((newRow, newCol, distance + 1))
        return -1
