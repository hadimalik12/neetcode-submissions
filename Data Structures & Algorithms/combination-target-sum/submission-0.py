class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        tot = 0

        def dfs(i, tot):
            if tot == target:
                res.append(sub.copy())
                return
            elif tot > target or i == len(candidates):
                return
            else:
                sub.append(candidates[i])
                dfs(i, tot + candidates[i])

                sub.pop()
                dfs(i + 1, tot)
        
        dfs(0, tot)
        return res
                

            
