class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        self.m, self.n = len(grid), len(grid[0])
        self.visited = {}
        def dfs(i, j):
            if (i, j) in self.visited or i < 0 or j < 0 or i == self.m or j == self.n or grid[i][j] == '0':
                return
            self.visited[(i, j)] = 1
            for x, y in [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]:
                dfs(x, y)
        count = 0
        for i in range(self.m):
            for j in range(self.n):
                if (i, j) not in self.visited and grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count
                
        
