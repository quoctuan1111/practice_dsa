class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        ans = 0
        seen = set()
        m = len(grid)
        n = len(grid[0])
        def dfs(grid, i, j):
            if (i < 0 or i >= m) or (j < 0 or j >= n) or grid[i][j] != '1' or (i, j) in seen:
                return 
            seen.add((i, j))
            dfs(grid, i - 1, j)  
            dfs(grid, i + 1, j)  
            dfs(grid, i, j - 1)  
            dfs(grid, i, j + 1)  
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and (i, j) not in seen :
                    ans += 1
                    dfs(grid, i ,j)
        return ans