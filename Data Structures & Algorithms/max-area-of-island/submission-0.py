class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.count = 0
        island = 0
        def dfs(i, j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0:
                return
            self.count += 1
            grid[i][j] = 0
            dfs(i-1, j) # Top
            dfs(i, j-1) # Left
            dfs(i+1, j) # Bottom
            dfs(i, j+1) # Right
    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs(i, j)
                    if self.count > island:
                        island = self.count
                    self.count = 0
        return island
