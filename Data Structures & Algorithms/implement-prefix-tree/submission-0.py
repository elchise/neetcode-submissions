class Node:
    def __init__(self):
        self.characters = {}
        self.end = False

class PrefixTree:

    def __init__(self):
        self.root = Node()        

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.characters:
                cur.characters[c] = Node()
            
            cur = cur.characters[c]
        
        cur.end = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.characters:
                return False
            cur = cur.characters[c]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.characters:
                return False
            cur = cur.characters[c]
        return True
        