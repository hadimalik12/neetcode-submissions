class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = r

        while l <= r:
            mid = l+(r-l)//2

            count = 0
            for i in piles:
                count += -(-i//mid)
        
            if count > h:
                l = mid + 1
            else:
                res = min(mid, res)
                r = mid - 1
            
        return res
                





