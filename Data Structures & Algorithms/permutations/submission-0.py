class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(perm, nums, vis):
            if len(perm) == len(nums):
                res.append(perm[:])
                return
            
            for i in range(len(nums)):
                if not vis[i]:
                    perm.append(nums[i])
                    vis[i] = True
                    dfs(perm, nums, vis)
                    perm.pop()
                    vis[i] = False
        
        dfs([], nums, [False] * len(nums))
        return res
            