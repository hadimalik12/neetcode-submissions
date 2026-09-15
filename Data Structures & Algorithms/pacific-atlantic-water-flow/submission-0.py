class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        atl = set()
        pac = set()
        rows = len(heights)
        cols = len(heights[0])

        def dfs(r, c, vis, prev):
            if (r, c) in vis or r < 0 or c < 0 or r == rows or c == cols or prev > heights[r][c]:
                return
            vis.add((r,c))
            dfs(r-1, c, vis, heights[r][c])
            dfs(r+1, c, vis, heights[r][c])
            dfs(r, c-1, vis, heights[r][c])
            dfs(r, c+1, vis, heights[r][c])
        
        for i in range(rows):
            dfs(i, 0, pac, 0)
            dfs(i, cols - 1, atl, 0)
        
        for j in range(cols):
            dfs(0, j, pac, 0)
            dfs(rows - 1, j, atl, 0)
        
        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r,c))
        
        return res

            