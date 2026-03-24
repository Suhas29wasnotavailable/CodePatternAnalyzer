class Solution:
    def numIslands(self,g):
        if not g:return 0
        r,c,cnt=len(g),len(g[0]),0
        def dfs(i,j):
            if 0<=i<r and 0<=j<c and g[i][j]=='1':
                g[i][j]='0'
                for di,dj in[(1,0),(-1,0),(0,1),(0,-1)]:dfs(i+di,j+dj)
        for i in range(r):
            for j in range(c):
                if g[i][j]=='1':cnt+=1;dfs(i,j)
        return cnt
