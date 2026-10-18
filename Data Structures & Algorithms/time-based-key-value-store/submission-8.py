from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.cache = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.cache[key].append((timestamp, value))
        # print(self.cache)

    def get(self, key: str, timestamp: int) -> str:
        values = self.cache[key]
        l, r = 0, len(values)-1
        mid = (l + r) // 2

        while l <= r:
            mid = (l + r) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
            
        
        return values[r][1] if r >= 0 else ""
