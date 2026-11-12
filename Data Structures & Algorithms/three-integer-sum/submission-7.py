class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(0, len(nums) - 2):
            j, k = i + 1, len(nums) - 1
            target = 0 - nums[i]
            print(nums[i], nums[j], nums[k])
            while j < k:
                if (nums[j] + nums[k]) == target:
                    if [nums[i], nums[j], nums[k]] not in res:
                        res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                elif (nums[j] + nums[k]) > target:
                    k-=1
                else:
                    j+=1
        return res
            