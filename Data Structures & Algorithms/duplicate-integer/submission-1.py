class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for i in nums:
            if hm.get(i) == 1:
                return True
            else:
                hm[i] = 1
        
        return False