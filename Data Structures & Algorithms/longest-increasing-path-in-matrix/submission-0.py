class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        dp = [[-1 for _ in range(cols)] for _ in range(rows)]
        res = 1

        def dfs(r, c):
            if dp[r][c] != -1:
                return dp[r][c]
            
            max_len = 1
            for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    max_len = max(max_len, 1 + dfs(nr, nc))
            
            dp[r][c] = max_len
            return max_len
        
        for r in range(rows):
            for c in range(cols):
                res = max(res, dfs(r,c))
        
        return res