class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm_s = {}
        hm_t = {}

        for i in s:
            hm_s[i] = hm_s.get(i, 0) + 1
        
        for j in t:
            hm_t[j] = hm_t.get(j, 0) + 1
        
        return hm_s == hm_t