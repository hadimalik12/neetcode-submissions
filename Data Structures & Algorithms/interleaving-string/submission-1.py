class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)

        if n + m != len(s3):
            return False
        
        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(1, m + 1):
            dp[0][i] = dp[0][i-1] and s2[i-1] == s3[i-1]
        
        for j in range(1, n + 1):
            dp[j][0] = dp[j-1][0] and s1[j-1] == s3[j-1]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if dp[i][j-1] and s2[j-1] == s3[i+j-1]:
                    dp[i][j] = True
                if dp[i-1][j] and s1[i-1] == s3[i+j-1]:
                    dp[i][j] = True
        
        return dp[n][m]