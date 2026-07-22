import random

class RandomizedSet:

    def __init__(self):
        self.valToInd = {}
        self.randSet = []

    def insert(self, val: int) -> bool:
        if val in self.valToInd:
            return False

        self.valToInd[val] = len(self.randSet)
        self.randSet.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.valToInd:
            return False
        
        ind = self.valToInd[val]
        self.randSet[ind] = self.randSet[-1]
        self.valToInd[self.randSet[-1]] = ind
        self.randSet.pop()
        del self.valToInd[val]
        return True

    def getRandom(self) -> int:
        i = random.randint(0, len(self.randSet) - 1)
        return self.randSet[i]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()