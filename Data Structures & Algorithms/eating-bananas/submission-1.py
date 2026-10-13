class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)

        prev = h
        res = r

        while l <= r:
            mid = l+(r-l)//2

            count = 0
            for i in piles:
                count += -(-i//mid)
            
            print(l, mid, r)
            if count > h:
                l = mid + 1
            else:
                if count <= h:
                    prev = count
                    res = min(mid, res)
                r = mid - 1
            print(count, prev, res)
            print('\n')
            
        return res
                





