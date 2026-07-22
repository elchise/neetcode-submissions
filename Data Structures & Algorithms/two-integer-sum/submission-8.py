class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for i in range(0, len(nums)):
            if not nums[i] in values:
                values[nums[i]] = []
            values[nums[i]].append(i)
        print(values)
        for i in values:
            if (target-i) in values:
                if (values[i] == values[target-i]) and (len(values[i]) > 1):
                    return[values[i][0], values[i][1]]
                elif values[i] == values[target-i]:
                    continue
                return [values[i][0], values[target-i][0]]
            

