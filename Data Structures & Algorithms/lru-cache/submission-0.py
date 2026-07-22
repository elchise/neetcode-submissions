class LRUCache:
    class Node:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.nxt = self.prv = None 

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head, self.tail = self.Node(0, 0), self.Node(0, 0)
        self.head.nxt = self.tail
        self.tail.prv = self.head 

    def insert(self, node):
        self.tail.prv.nxt = node
        node.prv = self.tail.prv
        self.tail.prv = node
        node.nxt = self.tail
    
    def remove(self, node):
        node.prv.nxt = node.nxt
        node.nxt.prv = node.prv

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        cur = self.cache[key]
        self.remove(cur)
        self.insert(cur)
        return cur.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            cur = self.cache[key]
            cur.value = value
            self.remove(cur)
            self.insert(cur)
        else:
            if len(self.cache) == self.capacity:
                self.cache.pop(self.head.nxt.key)
                self.remove(self.head.nxt)
                
            cur = self.Node(key, value)
            self.insert(cur)
            self.cache[key] = cur
        


        
