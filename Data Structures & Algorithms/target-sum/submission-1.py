class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        tot = sum(nums)
        if target > tot or (tot + target) % 2 == 1 or (tot + target) < 0:
            return 0
        target = (tot + target) // 2
        
        n = len(nums)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for j in range(target + 1):
                if nums[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i-1]]
        
        return dp[n][target]
