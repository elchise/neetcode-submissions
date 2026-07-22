from collections import Counter
from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Counts = defaultdict(int)
        counts = defaultdict(int)
        l = 0

        if len(s1) > len(s2):
            return False

        for c in s1:
            s1Counts[c] += 1

        print(s1Counts)
        for r in range(len(s1)):
            counts[s2[r]] += 1

        for r in range(len(s1), len(s2)):
            print(counts)
            if counts == s1Counts:
                return True
            
            counts[s2[r]] += 1
            counts[s2[l]] -= 1
            if counts[s2[l]] == 0:
                counts.pop(s2[l])

            l += 1

        return counts == s1Counts
