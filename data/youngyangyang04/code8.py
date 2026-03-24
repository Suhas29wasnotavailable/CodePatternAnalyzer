class Solution:
    def numIslands(self, grid):
        count = 0
        if grid is not None:
            if len(grid) > 0:
                for i in range(len(grid)):
                    if grid[i] is not None:
                        for j in range(len(grid[i])):
                            if grid[i][j] is not None:
                                if grid[i][j] == '1':
                                    count += 1
                                    self.dfs(grid, i, j)
        return count

    def dfs(self, grid, i, j):
        if i >= 0 and i < len(grid):
            if j >= 0 and j < len(grid[i]):
                if grid[i][j] is not None:
                    if grid[i][j] == '1':
                        grid[i][j] = '0'
                        self.dfs(grid, i + 1, j)
                        self.dfs(grid, i - 1, j)
                        self.dfs(grid, i, j + 1)
                        self.dfs(grid, i, j - 1)
