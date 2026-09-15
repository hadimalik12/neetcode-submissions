class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for s in strs:
            res += str(s) + "."
        return res
    def decode(self, s: str) -> List[str]:
        ans = s.split(".")
        ans.pop(-1)
        return ans

