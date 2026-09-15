class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        real = 0
        maxlen = 1
        dp = [[False] * n for _ in range(n)]

        if n <= 1:
            return s

        for i in range(n):
            dp[i][i] = True

        for i in range(2, n+1):
            for start in range(n - i + 1):
                end = start + i - 1

                if s[start] == s[end]:
                    if i == 2:
                        dp[start][end] = True
                    else:
                        dp[start][end] = dp[start+1][end-1]
                    if i > maxlen and dp[start][end]:
                        maxlen = i
                        real = start
                
                else:
                    dp[start][end] = False
        
        return s[real:real+maxlen]