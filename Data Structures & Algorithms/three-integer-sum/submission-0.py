class Solution:
    def threeSum(self, nums: List[int]):
        # Your code goes here
        nums.sort()
        res = []
        size = len(nums)
        for i in range(size - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                curr = nums[i] + nums[l] + nums[r]
                if curr == 0:
                    if [nums[i], nums[l], nums[r]] not in res:
                        res.append([nums[i], nums[l], nums[r]])
                if curr < 0:
                    l += 1
                else:
                    r -= 1
        return res
