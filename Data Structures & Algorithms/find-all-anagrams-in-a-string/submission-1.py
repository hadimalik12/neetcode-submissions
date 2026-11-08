class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hm = {}
        for i in p:
            hm[i] = hm.get(i, 0) + 1
        
        start = 0
        state = {}
        res = []

        for end in range(len(s)):
            state[s[end]] = state.get(s[end], 0) + 1
            if end - start + 1 == len(p):
                if state == hm:
                    res.append(start)
                
                state[s[start]] -= 1

                if state[s[start]] == 0:
                    del state[s[start]]
                
                start += 1
        
        return res

