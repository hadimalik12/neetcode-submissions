class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hm = {}

        for i in s:
            if i in hm:
                hm[i] += 1
            else:
                hm[i] = 1
        
        for j in t:
            if j in hm:
                hm[j] -= 1
                if hm[j] == 0:
                    del hm[j]
            else:
                return False
        
        if len(hm) == 0:
            return True
        else:
            return False
    
            