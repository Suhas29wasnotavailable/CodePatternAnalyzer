class Solution:
    def numIslands(self,grid):
     cnt=0
     for i in range(len(grid)):
         for j in range(len(grid[i])):
          if grid[i][j]=='1':
              cnt=cnt+1
              self.dfs(grid,i,j)
     return cnt
    def dfs(self,grid,i,j):
        if i<0 or i>=len(grid):
         return
        if j<0 or j>=len(grid[i]):
         return
        if grid[i][j]!='1':
            return
        grid[i][j]='0'
        self.dfs(grid,i+1,j)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i,j-1)
