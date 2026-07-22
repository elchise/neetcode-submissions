from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        freq = [[] for _ in range(len(nums)+1)]

        for num in nums:
            count[num] += 1
        
        for num, c in count.items():
            freq[c].append(num)
        
        i = len(freq) - 1
        res = []
        while k > 0:
            for num in freq[i]:
                res.append(num)
                k -= 1
            i -= 1
        
        return res

        
