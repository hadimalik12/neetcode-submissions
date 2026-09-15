class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        mid = (right - left) // 2

        while left < right:
            if nums[mid] > nums[right]:
                left = mid + 1
                mid = left + (right - left) // 2
            else:
                if nums[mid-1] > nums[mid]:
                    return nums[mid]
                
                right = mid
                mid = left + (right - left) // 2
        
        return nums[mid]