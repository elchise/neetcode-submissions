class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        vals = self.store[key]
        if vals[-1][0] <= timestamp:
            return self.store[key][-1][1]
        
        l, r = 0, len(vals)-1
        res = ""
        while l <= r:
            m = (l+r)//2
            if vals[m][0] == timestamp:
                return vals[m][1]
            elif vals[m][0] < timestamp:
                l = m + 1
                res = vals[m][1]
            else:
                r = m - 1
        
        return res
