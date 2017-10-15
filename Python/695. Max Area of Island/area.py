class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.max, self.cur = 0, 0
        self.visited = {}
        self.m, self.n = len(grid), len(grid[0])
        self.cur = 0
        def dfs(i, j):
            if (i, j) in self.visited or i >= self.m or i < 0 or j >= self.n or j < 0 or grid[i][j] == 0:
                return 
            self.visited[(i, j)] = True
            self.cur += 1
            for a, b in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                dfs(a, b)
        for i in range(self.m):
            for j in range(self.n):
                self.cur = 0
                dfs(i, j)
                self.max = max(self.max, self.cur)
        return self.max
            
            
        
