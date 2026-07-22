from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefSum = defaultdict(int)
        prefSum[0] = 1

        for num in nums:
            curSum += num
            dif =  curSum - k
            res += prefSum[dif]
            prefSum[curSum] += 1

        return res

