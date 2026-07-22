class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            count = [0]*26
            for ch in word:
                c = ord(ch) - ord('a')
                count[c] += 1
            res[tuple(count)].append(word)
        
        return list(res.values())
