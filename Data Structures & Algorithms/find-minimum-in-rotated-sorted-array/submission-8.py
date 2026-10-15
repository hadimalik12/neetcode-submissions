class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r-l)//2

            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] > nums[m-1]:
                r = m - 1
            else:
                return nums[m]
         
        return nums[m]