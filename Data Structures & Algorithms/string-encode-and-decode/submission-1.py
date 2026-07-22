class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += s
            res += "\n"
        return res

    def decode(self, s: str) -> List[str]:
        res = s.split("\n")
        return res[:len(res)-1]