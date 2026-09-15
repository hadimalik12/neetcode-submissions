class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        r, c = len(grid), len(grid[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        res = 0

        def dfs(x, y):
            if x < 0 or x == len(grid) or y < 0 or y == len(grid[0]) or grid[x][y] == '0':
                return
            
            grid[x][y] = '0'
            for row, col in directions:
                dfs(x + row, y + col)
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1':
                    dfs(i, j)
                    res+=1

        return res
            
