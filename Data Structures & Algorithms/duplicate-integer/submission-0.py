class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hm = {}
        for i in nums:
            hm[i] = hm.get(i, 0) + 1
            if hm[i] > 1:
                return True
        return False