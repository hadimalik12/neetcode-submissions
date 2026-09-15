class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        res = 0
        long = 0
        hm = {}

        for r, a in enumerate(s):
            hm[a] = hm.get(a, 0) + 1
            long = max(long, hm[a])

            while (r-l+1) - long > k:
                hm[s[l]] -= 1
                l += 1
            
            res = max(res, r-l+1)

        return res
            
