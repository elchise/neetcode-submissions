from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))
        # print(self.cache)

    def get(self, key: str, timestamp: int) -> str:
        values = self.cache[key]
        res = ""
        l, r = 0, len(values)-1
        mid = (l + r) // 2

        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] == timestamp:
                res = values[mid][1]
                break
            elif values[mid][0] < timestamp:
                res = values[mid][1]
                l = mid + 1
            elif values[mid][0] > timestamp:
                r = mid - 1
            
        return res
