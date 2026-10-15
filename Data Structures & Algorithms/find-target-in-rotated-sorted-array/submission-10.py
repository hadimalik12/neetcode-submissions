class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = l + (r-l)//2
            print(l, m, r)

            if nums[m] == target:
                return m
            elif nums[m] > nums[r]:
                if target > nums[m] or target <= nums[r]:
                    l = m + 1
                else:
                    r = m -1
            else:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
            
        return -1
